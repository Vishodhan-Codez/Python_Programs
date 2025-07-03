w = input("Enter the string : ")
sum = ""
for i in w :
    if i.islower() :
        i=i.upper()
        sum += i
    else :
        i=i.lower()
        sum += i
print(sum)
print(w.swapcase())
#.swapcase() is a function that swaps case