def tailrec(n,num) :
    if n > num :
        return
    print(n)
    tailrec(n+1,num)
n = int(input("Enter a number to print for n until : "))
tailrec(1,n)