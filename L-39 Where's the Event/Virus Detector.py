from tkinter import *
from tkinter import messagebox

win = Tk()
win.configure(bg="green")
win.title("Virus Detector")
win.geometry('500x500')

def msg() :
    win.configure(bg="red")
    messagebox.showwarning("Alert","Stop Virus Found !")
button= Button(bg="black",fg="white",text="Search for Virus !",command=msg)
button.pack()

win.mainloop()
