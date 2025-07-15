def GCD(a,b) :
    if b == 0 :
        return a
    return GCD(b,a%b)
print(GCD(int(input("Enter a number : ")),int(input("Enter another number : "))))