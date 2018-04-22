import sys
import sqlite3 as lite
import time

#run with python sign_outW.py id location state


con = lite.connect('sign_out.db')

def get_entry():
    entry_file = open('/Users/kulnahor/entry.txt', 'r')
    global entry_num
    entry_num = entry_file.read()
    entry_num = entry_num.rstrip()
    return entry_num
    entry_file.close()

def change_entry():
    entry_num = get_entry()
    print(entry_num)
    entry_file = open('/Users/kulnahor/entry.txt', 'w')
    entry_num = int(entry_num)
    entry_file.truncate()
    entry_num = entry_num+1
    entry_num = str(entry_num)
    entry_file.write(entry_num)
    entry_file.close()

with con:
    con.text_factory = str
    cur = con.cursor()

    argument = sys.argv

    #cur.execute('SELECT state FROM Users WHERE id = ? AND entry = entry_num = (SELECT MAX(entry_num) FROM Users)', [sys.argv[1]])
    #data = cur.fetchone()


    time = time.asctime()
    cur.execute('INSERT INTO Users VALUES(?, ?, ?, ?, "arriving")', (get_entry(), sys.argv[1], sys.argv[2], time))

    print('new entry added')
    print(cur.execute('SELECT * FROM Users'))

    change_entry()


con.close()
