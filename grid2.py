from tkinter import *
def getvals():
    print(f"the value of username is {uservalue.get()}")
    print(f"the value of username is {passvalue.get()}")
import tkinter as tk
root=tk.Tk()
root.iconphoto(False,tk.PhotoImage(file='2.png'))

root.geometry("300x400")

    
root.title("hello friends")

user=Label(root,text="username")
password=Label(root,text="password")
user.grid(row=0,column=1)
password.grid(row=1,column=1)

uservalue=StringVar()
passvalue=StringVar()

userentery=Entry(root,textvariable=uservalue).grid(row=0,column=2)
paswordentry=Entry(root,textvariable=passvalue).grid(row=1,column=2)
Button(text="submit",command=getvals).grid(column=3)
root.mainloop()