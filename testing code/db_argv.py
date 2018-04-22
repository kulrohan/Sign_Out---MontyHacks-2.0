import sys
import sqlite3 as lite

con = lite.connect('Rohandb.db')

#preset entry to 1

entry = open('/Users/kulnahor/entry.txt', 'r')
entry_num = entry.read()
entry_num = entry_num.rstrip()     #current entry number is the id for db
print(entry_num)
entry.close()

with con:

    con.text_factory = str

    cur = con.cursor()

    #cur.execute("DELETE FROM Family")  #Delete all previous record
    #cur.execute("CREATE TABLE Family(Id INT, Name TEXT, Relation TEXT)")

    arguments = sys.argv

    cur.execute("INSERT INTO Family (Id, Name, Relation) VALUES(?, ?, ?)", (entry_num, str(sys.argv[1].rstrip()), str(sys.argv[2].rstrip()),))

    print('new entry added')

    cur.execute("SELECT * FROM Family WHERE Id = (SELECT MAX(Id) FROM Family)")
    data = cur.fetchall()
    print(data)

#    cur.execute("SELECT Name FROM Family WHERE Id = (SELECT MAX(Id) FROM Family)")
    #data = cur.fetchone()
#    print(data)

    entry = open('/Users/kulnahor/entry.txt', 'w')
    print(entry_num)
    entry_num = int(entry_num)                          #delete all previous data, write new entry number (+1)
    entry.truncate()
    entry_num = entry_num+1
    entry_num = str(entry_num)
    entry.write(entry_num)
    entry.close()
