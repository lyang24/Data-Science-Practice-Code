import requests
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
import time
from dateutil.parser import parse 
import collections
import datetime


#IntegrityError: UNIQUE constraint failed: citibike_reference.id
url = 'http://www.citibikenyc.com/stations/json'
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
con = lite.connect('citi_bike.db')
cur = con.cursor()
# get data
def gcdata(url, sql, con, cur):
    r = requests.get(url)
    df = json_normalize(r.json()['stationBeanList'])
    exec_time = parse(r.json()['executionTime'])
    # set up sqlite3 connection
    # for loops populating data
    with con:
        cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%Y-%m-%dT%H:%M:%S'),))
        #for station in r.json()['stationBeanList']:
    #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
           # cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))
        for station in r.json()['stationBeanList']:
            

            cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + str((exec_time - datetime.datetime(1970,1,1)).total_seconds()) + ";")
            con.commit
    print('data imported')
# looping to retrive and analyze an hour of bike data
for times in range(60):
    gcdata(url, sql, con, cur)
    time.sleep(60)