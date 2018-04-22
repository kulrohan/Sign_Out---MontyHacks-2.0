from Tkinter import *
import sqlite3 as lite

con = lite.connect('sign_out.db')
cur = con.cursor()

def get_location():
    in_id = e1.get()
    cur.execute('SELECT loc, time, state FROM Users WHERE id = ? AND entry_num = (SELECT MAX(entry_num) FROM Users)', [in_id,])
    data = cur.fetchone()
    txt = "%s was last recorded at %s at %s" %(in_id, data[0], data[1])
    print(txt)

def get_log():
    in_id = e1.get()
    cur.execute('SELECT loc, time FROM Users WHERE id = ?', [in_id,])
    data = cur.fetchall()
    for x in range(1, len(data)):
        txt = "%s was recorded at %s at %s" %(in_id, data[x][0], data[x][1])
        print(txt)



def get_id():
    e1.get()

tk = Tk()

tk.resizable(width=False, height=False)
tk.geometry('{}x{}'.format(500,500))

Label(tk, text="Student ID:").grid(row = 0)
Label(tk).grid(row = 2)
Label(tk).grid(row = 3)
Label(tk).grid(row = 4)



e1 = Entry(tk)
e1.grid(row = 0, column = 1)


Button(tk, text = 'Get Location', command = get_location).grid(row = 0, column=2)
Button(tk, text = 'Get Log', command = get_log).grid(row = 0, column=3)







mainloop()
