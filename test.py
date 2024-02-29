import csv
import sqlite3
from datetime import datetime


#opening connection to the database/ creates database if not found
conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute('select * from matches')
matches = cur.fetchall()


for i in range(len(matches)):
  print(matches[i][7] == matches[i][7])