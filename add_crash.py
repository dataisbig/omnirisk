from server_connect import AccidentDB
from ftp_retrieval import AccidentArchiveFTP
import arrow

archive = AccidentArchiveFTP()
database = AccidentDB()

data = archive.get_file(archive.latest_upload.file.values[0])

data['REPORT_DATE'] = [arrow.get(i, 'DD-MMM-YY').format('YYYY-MM-DD') for i in data['REPORT_DATE'].values]

#TODO fix dates
print database.sql_add.format(*[i for i in data.iloc[0]])

print data.iloc[0]

database.add_accident([i for i in data.iloc[0]])

database.cursor.execute('SELECT * FROM accidents;')

print [i for i in database.cursor]