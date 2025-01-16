n = int(input("Enter a 4-Digit Number : "))
if (n > 1000) and (n < 9999) :
    n = str(n)
    n1 = int(n[1])
    n2 = int(n[2])
    print("The Number got is ",(n1*n2))
else  :
    print("Enter a valid 4 - digit number.")
    exit()
