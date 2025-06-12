b = int(input("Enter an number : "))
if b & b-1 == 0 :
    if b%10 == 4 or b%10 == 6 or b == 1:
        print("Its a power of 4")
        exit()
    else :
        print("Its not a power of 4")
        exit()
print("Its not a power of 4")
