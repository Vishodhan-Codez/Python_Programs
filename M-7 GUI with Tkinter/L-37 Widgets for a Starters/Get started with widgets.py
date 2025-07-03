from tkinter import *
from datetime import date
win = Tk()
win.title("Hello World")
win.geometry('600x400')

label = Label(win,text="Hi There",bg = "blue",fg="white",width=600)
anotherlabel = Label(win,text="Enter your name : ",bg = "#ADD8E6",fg="black",width=300)
input1 = Entry(win)
def display() :
    name = input1.get()
    global msg
    msg = "Hello "+name+"\n"
    msg2 = "Today's date is "+str(date.today())+"\n"
    msg3= "This is an example of widgets"+"\n"
    box.delete(1.0,END)
    box.insert(END,msg)
    box.insert(END,msg2)
    box.insert(END,msg3)
box = Text(win,width=400)
button = Button(win,text="Continue",bg="#80532d",fg="white",width=100,command=display)
label.pack()
anotherlabel.pack(pady=10)
input1.pack(pady=40)
button.pack(pady=10)
box.pack(pady=5)

win.mainloop()
