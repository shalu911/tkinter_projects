from tkinter import *
def getvals():
    print("its work")
import tkinter as tk
root=tk.Tk()
root.iconphoto(False,tk.PhotoImage(file="2.png"))
root.title("its my window shlzz")
#label for heading
label=Label(text="its for travel form",font="comiscansms 17 bold").grid(column=3)
#some label for only info
name=Label(root,text="name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
emergencyphone=Label(root,text="emergencyphone")
paymantmode=Label(root,text="paymantmode")
#pack
name.grid(row=1,column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergencyphone.grid(row=4, column=2)
paymantmode.grid(row=5, column=2)
# Tkinter variable for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymantmodevalue=StringVar()
foodservicevalue=IntVar()
#entry
nameentry=Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymantmodevalue)
# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)
#Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit to Harry Travels", command=getvals).grid(row=7, column=3)



root.mainloop()
