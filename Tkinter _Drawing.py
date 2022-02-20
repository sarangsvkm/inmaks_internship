from Tkinter import *
root=Tk()
canvas=Canvas(root,width=100,height=200)
canvas.pack()
newline=canvas.create_line(0,0,8,90)
newline1=canvas.create_line(8,5,9,180)
newline2=canvas.create_line(8,2,10,275)
root.mainloop()