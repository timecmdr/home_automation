#!/usr/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='logs',
    user='root',
    passwd='',
    host='localhost')
c = conn.cursor()

# Insert some example data.
c.execute("INSERT INTO logs_table (log_date,message,log_level)  VALUES (NOW(), 'testing the message',0)")
conn.commit()

# Print the contents of the database.
#c.execute("SELECT * FROM logs_table")
#print([(r[0], r[1]) for r in c.fetchall()])
