from tkinter import *
root=Tk()
root.geometry("332x456")
def hello():
    print("hello harry bhai kese ho")
def amazing():
     print("harry bhai your vidio is amazing ")
def best():
    print("you are best teacher")
def techer():
    print("your teching idea and way are very good")
frame=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
frame.pack(side=LEFT,anchor=NE)
b1=Button(frame,fg="red",text="hello",command=hello)
b1.pack(side=LEFT,padx=25)
b1=Button(frame,fg="red",text="amazing",command=amazing)
b1.pack(side=LEFT,padx=25)
b1=Button(frame,fg="red",text="skil",command=best)
b1.pack(side=LEFT,padx=25)
b1=Button(frame,fg="red",text="idea",command=techer)
b1.pack(side=LEFT,padx=25)
root.mainloop()