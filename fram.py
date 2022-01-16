from tkinter import *
from tkinter import font
root=Tk()
root.geometry("445x66")
f1=Frame(root,bg="blue",borderwidth=4,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="hello")
l.pack(pady=142)
l=Label(f2,text="hello vs code was open",font="Desired_font",fg="red")
l.pack()
root.mainloop()