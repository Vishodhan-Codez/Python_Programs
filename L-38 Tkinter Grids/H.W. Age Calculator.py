from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator App")
root.geometry("500x500")

frame = Frame(master=root, height=250, width=400, bg="#d0efff")
frame.place(x=20, y=0)

label1 = Label(frame, text="Date of Birth :", bg="#3895d3", fg="white", width=12)
label2 = Label(frame, text="Month :", bg="#3895d3", fg="white", width=12)
label3 = Label(frame, text="Year :", bg="#3895d3", fg="white", width=12)

entry1 = Entry(frame)
entry2 = Entry(frame)
entry3 = Entry(frame)

def display():
    try: # we have to use exception handling as the user might input something random and computer will return error
        day = int(entry1.get())
        month = int(entry2.get())
        year = int(entry3.get())
        birth_date = date(year, month, day)
        today = date.today()
        age = today.year - birth_date.year
        textbox.delete(1.0, END)
        if age <= 0: # we have to use exception handling as the user might input something random and computer will return error
            textbox.insert(END, "Invalid input. Please enter valid numbers.")
        else :
            textbox.insert(END, f"You are {age} years old.")
    except :
        textbox.delete(1.0, END)
        textbox.insert(END, "Invalid input. Please enter valid numbers.")

textbox = Text(root, bg="#bebebe", fg="black", height=3, width=50)

button = Button(root, text="Calculate Age", command=display, bg="red", fg="white")

label1.place(x=20, y=20)
entry1.place(x=150, y=20)

label2.place(x=20, y=80)
entry2.place(x=150, y=80)

label3.place(x=20, y=140)
entry3.place(x=150, y=140)

button.place(x=150, y=270)
textbox.place(x=20, y=320)

root.mainloop()
