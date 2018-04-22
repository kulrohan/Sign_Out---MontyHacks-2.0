import sqlite3 as lite

con = lite.connect('Rohandb.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM Users")
    data = cur.fetchone()
    print data
