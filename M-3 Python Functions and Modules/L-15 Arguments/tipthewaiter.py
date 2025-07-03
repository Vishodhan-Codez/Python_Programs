def tip_wai(a,b) :
    tip = a*(b/100)
    return f"{b}% of the bill (₹{a}) is ₹{tip}\nThe total bill is {a+tip}"
price = float(input("Enter the final amount on the bill : ₹"))
tips = int(input("Enter the percentage you want to tip : "))
print(tip_wai(price,tips))
