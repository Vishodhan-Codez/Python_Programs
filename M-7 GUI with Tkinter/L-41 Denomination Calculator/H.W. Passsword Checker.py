from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Length Converter App")
win.geometry("400x400")

lbl1 = Label(win, text="Welcome to the Password Strength Checker!", font=("Arial", 12), fg="blue")
lbl1.pack(pady=20)

lbl2 = Label(win, text="Enter your password:")
lbl2.pack(pady=10)

entry = Entry(win, show="*")
entry.pack(pady=5)

lbl3 = Label(win, text="", font=("Arial", 12))
lbl3.pack(pady=20)

def msg():
    x = messagebox.askquestion("Check", "Do you want to check the password strength?")
    if x == "yes":
        strength()

def strength():
    pwd = entry.get()
    ln = len(pwd)
    if ln <= 5:
        lbl3.config(text="Weak", fg="red")
    elif ln <= 8:
        lbl3.config(text="Medium", fg="orange")
    elif ln <= 12:
        lbl3.config(text="Strong", fg="green")
    else:
        lbl3.config(text="Very Strong", fg="darkgreen")

btn = Button(win, text="Check Strength", command=msg, bg="blue", fg="white")
btn.pack(pady=10)

win.mainloop()
