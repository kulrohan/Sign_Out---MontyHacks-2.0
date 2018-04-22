import sqlite3 as lite

#con = lite.connect('Rohandb.db')
con = lite.connect('test.db')

global id
id = 1

with con:

    con.text_factory = str

    cur = con.cursor()

    #cur.execute("DELETE FROM Family")  #Delete all previous record
    #cur.execute("CREATE TABLE Family(Id INT, Name TEXT, Relation TEXT)")

#    cur.execute('SELECT Relation FROM Family WHERE Name = "Swati"')  #GET LOG
#    data = cur.fetchall()
#    print(data)
    #cur.execute('SELECT * FROM Family')
    #data = cur.fetchall()
    #print(data)

    #cur.execute('SELECT Relation FROM Family WHERE Name = "Swati" AND Id = (SELECT MAX(Id) FROM Family)')  #GET LATEST RECORD
    #data = cur.fetchall()
    #print(data[0][0])
    cur.execute('SELECT Location,Time FROM Family WHERE Name = "Rohan" AND Entry = (SELECT MAX(Entry) FROM Family)')
    data = cur.fetchone()
    print('Rohan was last recorded at %s at %s' %(data[0], data[1])) #last record

    cur.execute('SELECT Location,Time FROM Family WHERE Name = "Rohan"')
    data = cur.fetchall()
    for x in range(0, len(data)):
        print("Rohan was at %s at %s" %(data[x][0], data[x][1]))   #log
