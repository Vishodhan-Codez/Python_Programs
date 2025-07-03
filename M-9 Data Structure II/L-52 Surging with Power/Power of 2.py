a = 0
ans = 0
b = int(input("Enter a number to check if a power of 2 : "))
while ans < b :
    ans = 1<<a
    if ans == b :
        print(f"{b} is a power of 2")
        break
    a += 1 
else :
    print(f"{b} is not a power of 2 ")
