foods = ["apple", "banana", "milk", "bread", "rice"]
prices = [20, 10, 50, 40, 100]
cart = []
total = 0
print("Welcome to the Store!\nHere are the available items:")
for i in range(len(foods)):
    print(f"{foods[i].upper()}: ₹{prices[i]}")
while True:
    print("\nWhat would you like to buy? Type 'done' to finish shopping.")
    itm = input("Enter item name: ").strip().lower()
    if itm == "done":
        break
    if itm in foods:
        idx = foods.index(itm)
        qty = int(input(f"How many {itm}(s) would you like to buy? "))
        cart.append([itm, qty, prices[idx]])
        print(f"{qty} {itm}(s) added to your cart.")
    else:
        print("Sorry, we don't have that item.")

print("\nYour Cart:")
for i in cart:
    c = i[1] * i[2]
    total += c
    print(f"{i[0].upper()} x{i[1]}: ₹{c}")
print(f"Total Bill: ₹{total}")

while True:
    paid = int(input("Enter payment amount: ₹"))
    if paid == total:
        print("Thank you for paying the exact amount! Have a great day!")
        break
    elif paid > total:
        print(f"Thank you! Here's your change: ₹{paid - total}. Have a great day!")
        break
    else:
        print(f"Insufficient payment. Please pay ₹{total - paid} more.")
