def nthbit(number,n) :
    if number&(1 << (n-1)) :
        print("\nSET")
    else :
        print("\nNOT SET")
nthbit(int(input("Enter a number : ")),int(input("Enter a bit to find : ")))