def On2(n):
    i = 0
    for j in range(n):
        for k in range(n) :
            i+= 1
            print("*",end="")
        print()
    print("When the value of 'n' is {},the number of iterations is equal to {}".format(n,i))
On2(10)
On2(5)
On2(2)

# We see that as the value of n increases , the time taken increases proprtionally by n^2