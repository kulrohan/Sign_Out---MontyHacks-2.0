import sqlite3 as lite
import sys

con = lite.connect('Rohandb.db')

global id
id = 1

with con:
    cur = con.cursor()

    cur.execute("DELETE FROM Family")  #Delete all previous record
    #cur.execute("CREATE TABLE Family(Id INT, Name TEXT, Relation TEXT)")

    con.text_factory = str  #takes care of unicode
    while True:

        print('Add entry? (y/n)')
        add = sys.stdin.readline()
        add = add.rstrip()

        if add == 'y':
            print('Name')
            name = sys.stdin.readline()
            name = name.rstrip()
            print('relation')
            rel = sys.stdin.readline()
            rel = rel.rstrip()

            cur.execute("INSERT INTO Family (Id, Name, Relation) VALUES(?, ?, ?)", (id, name, rel,))

            print('new entry added')
            cur.execute("SELECT * FROM Family WHERE Id = (SELECT MAX(Id) FROM Family)")
            data = cur.fetchone()
            print(data)

            id = id +1

        if add == 'n':
            print('Database:')
            cur.execute("SELECT * FROM Family")
            data = cur.fetchall()
            print(data)
            break
