from tkinter import *
from tkinter import messagebox
shivay_root = Tk() #TK is class
num1=Entry(shivay_root)
num1.grid(row=0,column=1)
num2=Entry(shivay_root)
num2.grid(row=1,column=1)
# Label Widgets
l1 = Label(shivay_root,text="Enter Num 1:")
l1.grid(row=0,column=0)
Label(shivay_root,text="Enter Num 2:").grid(row=1)
def closeshivay_root():
    shivay_root.destroy()
def calculatesum():
    # print(float(num1.get())+float(num2.get()))
    result = float(num1.get()) + float(num2.get())
    Label(shivay_root,text="The Sum is {} ".format(result)).grid(row=10)
    messagebox.showinfo("The Sum is ",result)
    pass

Button(shivay_root,text="Exit",command=closeshivay_root).grid(row=5)
Button(shivay_root,text="Sum",command=calculatesum).grid(row=3)

#run the loop
shivay_root.mainloop()
