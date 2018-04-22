import sqlite3 as lite

con = lite.connect('sign_out.db')
cur = con.cursor()

with con:
    cur.execute('DELETE FROM Users;')

    cur.execute('INSERT INTO Users VALUES(0, 103488, "undef", "undef", "arriving")')
    cur.execute('INSERT INTO Users VALUES(0, 100863, "undef", "undef", "arriving")')
    cur.execute('INSERT INTO Users VALUES(0, 107739, "undef", "undef", "arriving")')
    cur.execute('INSERT INTO Users VALUES(0, 101867, "undef", "undef", "arriving")')
    cur.execute('INSERT INTO Users VALUES(0, 109425, "undef", "undef", "arriving")')

con.close()
