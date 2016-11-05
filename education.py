from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import statsmodels.api as sm


# get raw html
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
def make_soup(url):
    r = requests.get(url)
    soupdata = BeautifulSoup(r.content, 'html.parser')
    return soupdata
soup = make_soup(url)


rows = []
data = soup('table')[6] # I feel like i am hard coding this
for record in data.find_all('tr')[8:]:
    rows.append([val.text.encode('utf8') for val in record.find_all('td')])

 with open('C:\Users\Eric Yang\Desktop\out.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(row for row in rows) #DATA IS NOT PERFECT

import sqlite3 as lite

con = lite.connect('edu.db')
cur = con.cursor()

with con:
    cur.execute('CREATE TABLE edulife (country TEXT PRIMARY KEY, year INTEGER, male_avg INTEGER, female_avg INTEGER);')

with open('C:\Users\Eric Yang\Desktop\out.csv','rU') as inputFile1:
    inputReader1 = csv.reader(inputFile1)

import sqlite3 as lite


with con:
	#cur.execute('DROP TABLE gdp;')
    cur.execute('CREATE TABLE gdp (country_name TEXT,Country Code TEXT PRIMARY KEY, _1999 REAL, _2000 REAL, _2001 ,REAL _2002 REAL, _2003 REAL, _2004 REAL, _2005 REAL, _2006 REAL, _2007 REAL, _2008 REAL, _2009 REAL, _2010 REAL);')  



with open('C:\Users\Eric Yang\Desktop\API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv','rU') as inputFile:
    next(inputFile) # skip the first 3 lines
    next(inputFile)
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        with con:
            cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[43:55]) + '");') 

with con:
    cur.execute('SELECT * FROM gdp INNER JOIN edulife ON edulife.country = gdp.country_name;')
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

#check if data is imported correctly
#with con:
    #for row in cur.execute('SELECT * FROM gdp;'):
        #print (row)

# the data set is finished use regression to test out if gdp is correlated with education life.