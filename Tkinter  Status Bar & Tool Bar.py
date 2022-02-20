from tkinter import *
root=Tk()
def fun1():
    print("clicked")
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="save",command=fun1)
submenu.add_command(label="new",command=fun1)
submenu.add_separator()
submenu.add_command(label="open",command=fun1)
submenu.add_command(label="close project",command=fun1)
newmenu=Menu(root)

mymenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label="undo",command=fun1)

toolbar=Frame(root,bg='pink')
inbutton=Button(toolbar,text="crop")
inbutton.pack(side=TOP,padx=5,pady=6)
stauesbar=Label(root,text="this is bar", relief=SUNKEN,bd=10,anchor=W,)
stauesbar.pack(side=BOTTOM,fill=X)
toolbar.pack(side=TOP,fill=X)

root.mainloop()