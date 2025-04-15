from tkinter import *
win = Tk()
win.title("Length Converter")
win.geometry("300x200")

def convert(e):
    val = float(ent.get())
    cm = val * 2.54
    lbl.config(text=str(cm) + " cm") # converts the value of centimeter into string and adds cm at the end

ent = Entry()
ent.pack()
btn = Button(fg="white",bg="blue",text="Convert")
btn.pack()

lbl = Label(text="")
lbl.pack()

btn.bind("<Button-1>", convert)

win.mainloop()
