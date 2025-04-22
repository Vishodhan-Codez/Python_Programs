from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

window = Tk()
window.title("Notepad")
window.geometry("650x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

def open1() :
    filepath= askopenfilename(filetypes= [("Text Files","*.txt"),("All Files","*.*") ])
    if not filepath : 
        return 
    else :
        textedit.delete(1.0,END)
        with open(filepath,"r") as input_1 :
            filetext = input_1.read()
            textedit.insert(END,filetext)
            input_1.close()

def save1() :
    filepath= asksaveasfilename(defaultextension="txt",filetypes= [("Text Files","*.txt"),("All Files","*.*") ])
    if not filepath : 
        return 
    else :
        with open(filepath,"w") as input_1 :
            text = textedit.get(1.0,END)
            input_1.write(text)
            input_1.close()
textedit = Text(window)
fr_buttons = Frame(window,relief=RAISED,bd=2)
op = Button(fr_buttons,text="Open File",command=open1)
sv = Button(fr_buttons,text="Save As ...",command=save1)

op.grid(column=0,row=0,stick="ew",padx=5,pady=5)
sv.grid(column=0,row=1,stick="ew",padx=5)

fr_buttons.grid(column=0,row=0,sticky="ns")
textedit.grid(column=1,row=0,sticky="nsew")

window.mainloop()