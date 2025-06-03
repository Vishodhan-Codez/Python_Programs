def noofbits(n):
    count = 0
    while (n) :
        count += 1 
        n >>= 1
    print("The no of bits in the number are ",count)
noofbits(int(input("Enter a number for n : ")))