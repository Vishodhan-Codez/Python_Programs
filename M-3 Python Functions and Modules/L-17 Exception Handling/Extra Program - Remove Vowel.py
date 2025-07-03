nm = input("Enter your name : ")
nm = nm.upper()
k = ""
for i in nm :
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" :
        continue
    else :
        k += i
print(k)