from tkinter import *
from PIL import Image,ImageTk

root= Tk()

root.geometry("733x4340")

root.minsize(733,434)
root.maxsize(733,434)
image=Image.open("oklabs.ppg")
image = image.resize((30, 40),Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
 
photo=ImageTk.PhotoImage(image)
label = Label(image = photo)
label.pack()
welcome_message = Label(text="WELCOME TO MY CHENNAL OKLABS")
blank_space = Label(text="                                   ")
option1 = Label(text="OPEN THIS CHENNAL")
option2 = Label(text="SUBSCRIBED ")
option3 = Label(text= "COMPLETE ASSIGNMENT ")

welcome_message.pack()
blank_space.pack()
blank_space.pack()
option1.pack()
# blank_space.pack()
option2.pack()
# blank_space.pack()
option3.pack()

root.mainloop()