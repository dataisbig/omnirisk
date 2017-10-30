from ftplib import FTP
import arrow
import pandas as pd
import zipfile
import os


class AccidentArchiveFTP:

    def __init__(self):
        self.ftp = FTP("ftp.senture.com")
        self.ftp.login()
        self.ftp.cwd("Archive")
        self.files = []
        self.populate_index()


    def populate_index(self):
        f_temp = []
        self.ftp.dir(f_temp.append)
        for i in f_temp:
            if 'Crash' in i:
                i = i.split(' ')
                time = arrow.get(i[0]+' '+i[2][:-2]+' '+i[2][-2:], 'MM-DD-YY HH:mm A')

                self.files.append([time, int(i[-2]), i[-1]])
        self.files = pd.DataFrame(self.files, columns=['published', 'size', 'file'])

    @property
    def latest_upload(self):
        return self.files[self.files.published == self.files.published.max()]

    def get_file(self, filename):
        # download the desired file from the ftp server
        try:
            message =self.ftp.retrbinary("RETR "+filename, open('temp.zip', 'wb').write)
        except:
            self.ftp = FTP ("ftp.senture.com")
            self.ftp.login()
            self.ftp.cwd("Archive")
            message = self.ftp.retrbinary ("RETR " + filename, open ('temp.zip', 'wb').write)

        # unzip the files
        zip_file = zipfile.ZipFile('temp.zip')
        zip_file.extractall('.')
        files = zip_file.namelist()
        zip_file.close ()
        os.remove ('temp.zip')
        # why on earth did they need to use iso encoding?
        f = open([i for i in files if 'Read' not in i][0], 'r') # encoding='iso-8859-15')
        # get the data columns and
        head = f.readline().split('","')
        # annoying text fixes
        head[0] = head[0][1:]
        # remove extra escape char and quote
        head[-1] = head[-1][:-2]
        # these files were formatted by apes! APES!
        data = []
        for line in f.readlines():
            l = []
            line = line.split(',')
            # people who punctuate strings in CSV files with commas should be shot
            for i in line:
                i=i.replace('"', '')

                if len(i) is 0:
                    l.append(None)
                elif i[0] is ' ':
                    l[-1] += i
                else:
                    l.append(i)
            # remove extra escape char
            l[-1]=l[-1][:-2]

            data.append(l)


        # Close files and clean up
        f.close()
        for i in files:
            os.remove(i)

        data = pd.DataFrame(data, columns=head)
        data['TOW_AWAY'].replace('Y', '1', inplace=True)
        data['TOW_AWAY'].replace('N', '0', inplace=True)


        return data


