import pandas as pd 
import datetime as dt 
import requests
import sqlite3 as lite
con = lite.connect('weather.db')
cur = con.cursor()
cities.keys()
#set up table
#with con:
    #cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, Atlanta REAL, Austin REAL, Boston REAL, Chicago REAL, Cleveland REAL);')
api_key = '042476534a83cd8a28fd35226ad56eb7'

cities ={ "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }
for i, j in cities.iteritems():
    while qry_date < datetime.datetime.now():
        url = 'https://api.forecast.io/forecast/' + api_key + '/' + i + ',' + qry_date.strftime('%Y-%m-%dT12:00:00') # /LATITUDE,LONGITUDE,TIME
        r = requests.get(url)
        with con:
            cur.execute('UPDATE daily_temp SET ' + j + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%d'))
        qry_date += datetime.timedelta(days =1)
con.close
#ValueError: No JSON object could be decoded? server data error?
