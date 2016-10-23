import sqlite3 as lite
import pandas as pd

#preload data
cities = (('New York City', 'NY'),
('Boston', 'MA'),
('Chicago', 'IL'),
('Miami', 'FL'),
('Dallas', 'TX'),
('Seattle', 'WA'),
('Portland', 'OR'),
('San Francisco', 'CA'),
('Los Angeles', 'CA'),
('Washington', 'DC'),
('Hoston', 'TX'),
('Las Vegas', 'NV'),
('Atlanta', 'GA'))


weather = (('New York City',2013,'July','January',62),
  ('Boston',2013,'July','January',59),
  ('Chicago',2013,'July','January',59),
  ('Miami',2013,'August','January',84),
  ('Dallas', 2013,'July','January',77))
 
con = lite.connect('test.db')



# Set up database(create tables and insert prepared value)
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities;")
    cur.execute("DROP TABLE IF EXISTS weather;")
    cur.execute("CREATE TABLE cities (name text, state text);")
    cur.execute("CREATE TABLE weather ('city' text, 'year' integer, 'warm_month' text, 'cold_month' text,'average_high' integer);")
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    #join tables and load data into pandas data frames
    cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather  ON name = city;")
    
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    

