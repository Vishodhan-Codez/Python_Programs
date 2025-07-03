from tkinter import *
import random

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")
window.configure(bg="lightgrey")

choices = ["Rock", "Paper", "Scissors"]

def play(choice):
    comp = random.choice(choices)
    lbl_user.config(text=f"You: {choice}")
    lbl_comp.config(text=f"Computer: {comp}")
    if choice == comp:
        lbl_result.config(text="Draw")
    elif (choice == "Rock" and comp == "Scissors") or (choice == "Paper" and comp == "Rock") or (choice == "Scissors" and comp == "Paper"):
        lbl_result.config(text="You Win :)")
    else:
        lbl_result.config(text="You Lose :(")

Label(window, text="Rock Paper Scissors", bg="lightgrey", font=("Arial", 18, "bold")).pack(pady=20)

btn_frame = Frame(window, bg="lightgrey")
btn_frame.pack(pady=10)
Button(btn_frame, text="Rock", width=10, height=2, command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Paper", width=10, height=2, command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
Button(btn_frame, text="Scissors", width=10, height=2, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

lbl_user = Label(window, text="You: ", bg="lightgrey", font=("Arial", 12))
lbl_user.pack(pady=10)

lbl_comp = Label(window, text="Computer: ", bg="lightgrey", font=("Arial", 12))
lbl_comp.pack(pady=5)

lbl_result = Label(window, text="", bg="lightgrey", font=("Arial", 14, "bold"))
lbl_result.pack(pady=20)

window.mainloop()
