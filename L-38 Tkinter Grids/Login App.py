from tkinter import *
root = Tk()
root.title("Login App")
root.geometry("500x500")

frame = Frame(master=root,height=250,width=250,bg="#d0efff")

label1 = Label(frame,text="Full Name : ",bg="#3895d3",fg="white",width=12)
label2 = Label(frame,text="Email Id : ",bg="#3895d3",fg="white",width=12)
label3 = Label(frame,text="Password : ",bg="#3895d3",fg="white",width=12)

entry1 = Entry(frame)
entry2 = Entry(frame)
entry3 = Entry(frame,show="*")

def display() :
    name = entry1.get()
    greet = "Hey " + name
    msg = "\nCongratulations on your new account !"
    textbox.insert(END,greet)
    textbox.insert(END,msg)

textbox = Text(bg="#bebebe",fg="black")

button = Button(text="Create Account",command=display(),bg="red")

frame.place(x=20, y=0)

label1.place(x=20, y=20)

entry1.place(x=150, y=20)

label2.place(x=20, y=80)

entry2.place(x=150, y=80)

label3.place(x=20, y=140)

entry3.place(x=150, y=140)

button.place(x=130, y=210)
textbox.place(y=250)
root.mainloop()
