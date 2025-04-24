from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Order Menu")
window.configure(bg="lightgrey")
window.geometry("500x500")

menu = {
    "Idli" : 99,
    "Roti" : 119,
    "Naan" : 159,
    "Rice" : 45,
    "Dosa" : 129,
    "Gravy" : 199,
    "Vada Pav" : 49
}
order = []

def addorder(item,price) :
    order.append((item,price))
    upd_order()

def upd_order() :
    txt.delete(1.0,END)
    for item,price in order :
        txt.insert(END,f'{item:<10}₹{price}\n')
    ttlfunc()
    
def ttlfunc() :
    total = sum(price for _,price in order)
    totallabel.config(text=f"Total is ₹{total}")

def placeorder() :
    total = sum(price for _,price in order)
    if order :
        messagebox.showinfo("Order Successfull",f"Order has been Placed ,You have to pay ₹{total}")
    else :
        messagebox.showinfo("No Values","Please enter some items to proceed")
def clrorder() :
    order.clear()
    txt.delete(1.0,END)
    ttlfunc()

for idx,(items,price) in enumerate(menu.items()) :
    Button(window,text=f"{items}: ₹{price}",command=lambda i = items, p = price: addorder(i,p)).grid(row=idx+1,column= 0 ,padx=10,pady=10 )
Label(window,text="Order Summary").grid(row=0,column = 1 ,padx=10,pady=10)
txt = Text(window,height=15,width=30)
txt.grid(row=1,column=1,rowspan=6,padx=20)
totallabel= Label(window,text="Total : ₹0 ")
totallabel.grid(row=7,column=1,pady=10)
Button(window,text="Place Order",bg="red",fg="gray",width=15,command=placeorder).grid(row=8,column=1,sticky="w",padx=20)
Button(window,text="Clear",bg="red",fg="gray",width=15,command=clrorder).grid(row=8,column=1,sticky="e",padx=20)


window.mainloop()

