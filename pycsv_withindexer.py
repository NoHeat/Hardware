from __future__ import print_function
import sqlite3
import csv
import os
import glob
import sys
 
db = sys.argv[1]

conn = sqlite3.connect(db)
conn.text_factory = str  # allows utf-8 data to be stored
 
c = conn.cursor()

# traverse the directory and process each .csv file
for csvfile in glob.glob(os.path.join(sys.argv[2], "*.csv")):
#for csvfile in glob.glob("*.csv"):

    # remove the path and extension and use what's left as a table name
    tablename = "Main"
	
	#open csvfile and run thru for loop
    with open(csvfile, "rb") as f:
        reader = csv.reader(f)
 
	sql = "DROP TABLE IF EXISTS %s" % tablename
        c.execute(sql)
				#create table for data
        sql = "CREATE TABLE %s (Name, Category, Amount, H, L, E)" % tablename
        c.execute(sql)
        for row in reader:
				#insert csv data for each column in a row
            for column in row:
                insertsql = "INSERT INTO %s VALUES (%s)" % (tablename, ", ".join([ "?" for column in row ]))
	    c.execute(insertsql, row)

    conn.commit()

c.close()
conn.close()