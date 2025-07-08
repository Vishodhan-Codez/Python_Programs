def incdec(n,num):
    if (n > num) or (n < 1) :
        return
    print(n)
    incdec(n-1,num)
    print(n)
n = int(input("Enter a number to print for n until : "))
incdec(n,n)
    