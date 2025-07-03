n = int(input("Enter a natural number to add until : "))
if n < 0:
    print("Enter a number above 1 ")
    n = int(input("Enter a natural number to add until : "))
else :
    i,sum = 1,0
    while n >= i :
        sum += i
        i += 1
    print("The sum is ",sum)

