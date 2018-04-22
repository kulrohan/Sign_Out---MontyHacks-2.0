from Tkinter import *
import sqlite3 as lite

con = lite.connect('sign_out.db')
cur = con.cursor()

tk = Tk()

def get_location():
    in_id = e1.get()
    cur.execute('SELECT loc, time, state FROM Users WHERE id = ? AND entry_num = (SELECT MAX(entry_num) FROM Users)', [in_id,])
    data = cur.fetchone()
    txt = "%s was l" %(in_id)
    Label(tk, text=txt).grid(row = 4)


def get_id():
    e1.get()

tk.resizable(width=False, height=False)
tk.geometry('{}x{}'.format(500, 500))
Label(tk, text="First Name").grid(row=0)
Label(tk, text="Last Name").grid(row=1)
Label(tk)

e1 = Entry(tk)
e2 = Entry(tk)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Label(tk).grid(row=3)
Label(tk).grid(row=4)
Label(tk).grid(row=5)

Label(tk, width=5).grid(row=0, column=2)
Button(tk, text='Display', command = get_location).grid(row=0, column=3)




e1 = Entry(tk)
e1.grid(row = 0, column = 1)


#Button(tk, text = 'Get Location', command = get_location).grid(row = 0, column=2)
#Button(tk, text = 'Get Log', command = get_location).grid(row = 0, column=3)







mainloop()
