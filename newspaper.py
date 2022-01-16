from tkinter import *
from  PIL import Image,ImageTk

root = Tk()
root.geometry('1200x1200')
root.title('''khaber chuti tamasha bara''')

label=Label(text='''                                
DAILY MP
             1-1-22
''',bg='purple',font='cocmos 30 bold').pack()

label_1=Label(text='''A.I news''',bg='blue',font='cosmos 15 bold').pack()

image=Image.open('oklabs.jpg',)
photo=ImageTk.PhotoImage(image)

label_2=Label(image=photo).pack(side=LEFT,anchor='nw',pady=50)
label_2=Label(text='''
        A.I IN THICKING
If i call level A.I is another name ofthinking it's not wrong the reson s comman if we compare thinking we go far and farin that 
as a new information come by thinking more and more and we makeour self more better and better in that as for A.I do some as we 
see modern robots and software i mean how brilliant now days youtubeand google are ys you type such words and get 
whole line''',padx='1',pady='2',font='cosmos 7 bold').pack(side=TOP,anchor='nw',pady=33)

image_2=Image.open ('1.png')
photo_2=ImageTk.PhotoImage(image_2)

label_3=Label(image=photo_2).pack(side=RIGHT,anchor='nw')


label_4=Label(text='''
                                            A.I IN TIKTOK     
as we all know A.I is a chinese company and chinese are the the people which in a few years take lead in the import of 
the world and becouse with in few year world will geather in digital plateform and mean A.I chines take the lead one of
another reason is that thebig think tank says "where data is new oil for the world china is newsaudia arab" after read 
this line the greate sign for whose havegraete level of intelligence. china give there great to for A.I as if we take
example of ALIBABA the grete chines company have put alot in to take business dependend in A.I although you known what
it's CEO JACK MA tell we don't call this ARTIFICIAL INTELLIGENCE he have anothere name for it and it is "ALI BABA
INTELLIGENCE" it's sound fun but if we take a little view to it's psycology the this type of world that time when it go
so far in that perticuler thing or he has invented or already applying future technique in it and becouse of this he has
a clear view of it's leader ship in that thing so he ty to put there name in that thing as we know invention by the name
of these scientist although it's my view you can disagree with that.so taking aboutTIKTOK so it hase very relatable with
YOUTUBE and GOOGLE. the same pattern thst to see customer a product as a choice.and they starting playing with there mind.
''',padx=350,font=("cosmos 7 bold" )).pack(side=TOP,anchor='sw',padx=20)




root.mainloop()