def Flipbits(a,b) :
    flips = 0
    while a > 0 or b > 0 :
        t1 = a & 1 
        t2 = b & 1
        if t1 != t2 :
            flips += 1 
        a >>= 1 
        b >>= 1
    return flips
a = int(input("Enter a number : "))
a1 = a
b = int(input("Enter another number : "))
b1 = b
print(f"The no. of flips required to equalize {a1} and {b1} is {Flipbits(a,b)}")