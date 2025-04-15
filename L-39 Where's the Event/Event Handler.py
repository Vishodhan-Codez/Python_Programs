from tkinter import *
win = Tk()
win.title("Events")
win.geometry("400x400")

def button_click(event) :
    print("The button is clicked")
def charac(c) :
    print(c.char)

button = Button(bg="blue",fg="white",text="Click Me !")
button.pack()
win.bind("<Key>",charac)
button.bind("<Button-1>",button_click)

win.mainloop()