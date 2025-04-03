from tkinter import *
win = Tk()
win.title("Multiply Two Numbers")
win.geometry("300x200")

def calc():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        output_label.config(text=f"Product: {result}")
    except ValueError:
        output_label.config(text="Invalid input! Please enter numbers.")

Label(win, text="Enter first number:").pack(pady=5)
entry1 = Entry(win)
entry1.pack(pady=5)
Label(win, text="Enter second number:").pack(pady=5)
entry2 = Entry(win)
entry2.pack(pady=5)

Button(win, text="Calculate", command=calc).pack(pady=10)
output_label = Label(win, text="Product: ")
output_label.pack(pady=5)
win.mainloop()