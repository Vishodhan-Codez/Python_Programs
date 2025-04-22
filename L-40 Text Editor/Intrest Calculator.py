from tkinter import *

def calc():
    p = float(e1.get())
    r = float(e2.get())
    t = float(e3.get())

    si = (p * r * t) / 100
    ci = p * ((1 + r / 100) ** t) - p

    l4.config(text=f"SI: ₹{si:.2f}\nCI: ₹{ci:.2f}")

window = Tk()
window.title("Interest Calculator App")
window.geometry("400x400")

l1 = Label(window, text="Principal")
l1.grid(row=0, column=0, pady=10, padx=10, sticky=W)
e1 = Entry(window)
e1.grid(row=0, column=1)

l2 = Label(window, text="Rate")
l2.grid(row=1, column=0, pady=10, padx=10, sticky=W)
e2 = Entry(window)
e2.grid(row=1, column=1)

l3 = Label(window, text="Time")
l3.grid(row=2, column=0, pady=10, padx=10, sticky=W)
e3 = Entry(window)
e3.grid(row=2, column=1)

b1 = Button(window, text="Calculate", command=calc)
b1.grid(row=3, column=0, columnspan=2, pady=20)

l4 = Label(window, text="", font=("Arial", 12))
l4.grid(row=4, column=0, columnspan=2)

window.mainloop()
