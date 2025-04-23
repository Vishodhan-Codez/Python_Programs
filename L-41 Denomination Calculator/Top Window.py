from tkinter import *

window = Tk()
window.title("ROOT Window")
window.geometry("500x500")
def topwin() :
    win2 = Toplevel()
    win2.title("Top Window")
    win2.geometry("400x100")

    lab= Label(win2,text="This is the top window !! ")
    lab.pack()
    win2.mainloop()

lable = Label(window,text="This is the regular window !")
buttun = Button(window,bg="blue",fg="white",text="Click Me !",command=topwin)

lable.pack()
buttun.pack()

window.mainloop()