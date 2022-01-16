from tkinter import *
# from playsound import playsound
def shiv(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

import tkinter as tk
root=tk.Tk()
root.geometry("688x566")
# playsound('song.mp3')
root.title("its amazing")
root.iconphoto(False,tk.PhotoImage(file="2.png"))
Widget=Button(root,text="click as like you are haker")
Widget.grid()
Widget.bind('<Button-1>',shiv)
Widget.bind('<Double-1>', quit)
Widget.bind('<FocusIn>')


root.mainloop()