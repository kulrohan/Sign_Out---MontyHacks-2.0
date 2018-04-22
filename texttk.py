from Tkinter import *

tk = Tk()

def display_text():
    Label(tk, text=e1.get()).grid(row=5)

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
Button(tk, text='Display', command = display_text).grid(row=0, column=3)

mainloop()
