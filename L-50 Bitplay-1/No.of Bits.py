def no_of_bits(n) :
    ones = 0
    zeroes = 0
    while (n) :
        if (n&1)==1 :
            ones += 1 
        else :
            zeroes += 1 
        n>>=1
    print("The number of ones are",ones,"\nThenumber of zeroes are",zeroes)
no_of_bits(int(input("Enter a number : ")))
