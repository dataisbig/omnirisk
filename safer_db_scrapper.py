import re
from mechanize import Browser
from bs4 import BeautifulSoup

def scrapper(dot_num):
    browser = Browser ()
    browser.open ("https://safer.fmcsa.dot.gov/CompanySnapshot.aspx")

    browser.select_form (nr=0)
    browser["query_string"] = dot_num

    response = browser.submit ()

    content = response.read ()

    soup = BeautifulSoup(content, "lxml")

    rows = soup.findAll('tr')

    # Creates a 2-D matrix.
    for row in range (len (rows)):
        for name, info in zip(rows[row].findAll('th', {'class':'querylabelbkg'}), rows[row].findAll('td', {'class': 'queryfield'})):
            print name.getText()
            print info.getText()

        # Add each team to a teams matrix.

if __name__ == '__main__':
    scrapper('825773')