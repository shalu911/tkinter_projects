from tkinter import *
from PIL import Image,ImageTk
import os
root=Tk()
root.geometry("300x300")
image=Image.open("1.png")
photo=ImageTk.PhotoImage(image)
label = Label(image = photo)
label.pack()
dirs=os.listdir()
label2=Label(text=dirs)
label2.pack()
root.mainloop()