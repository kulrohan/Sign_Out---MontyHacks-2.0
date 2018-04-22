import sqlite3 as lite
import sys

con = lite.connect('sign_out.db')
cur = con.cursor()

with con:
    def get_location(in_id):
        cur.execute('SELECT loc, time FROM Users WHERE id = ? AND entry_num = (SELECT MAX(entry_num) FROM Users)', [in_id,])
        data = cur.fetchone()
        txt = "%s was last recorded at %s at %s" %(in_id, data[0], data[1])
        print(txt)

    def get_log(in_id):
        cur.execute('SELECT loc, time FROM Users WHERE id = ?', [in_id,])
        data = cur.fetchall()
        for x in range(1, len(data)):
            txt = "%s was recorded at %s at %s" %(in_id, data[x][0], data[x][1])
            print(txt)

    in_id = int(sys.stdin.readline())

    get_location(in_id)
    get_log(in_id)
