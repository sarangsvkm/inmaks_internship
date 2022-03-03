from tkinter import *
root = Tk()
def fun():
    print("click")

Label(root, text='First Name').grid(row=0)
Label(root, text='Last Name').grid(row=1)
Label(root, text='User Name').grid(row=2)
Label(root, text='password').grid(row=3)
bt1=Button(root,text="submit",command=fun)
bt1.grid(row=4,column=1)
bt2=Button(root,text="cancel",command=fun)
bt2.grid(row=4,column=2)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

root.mainloop()