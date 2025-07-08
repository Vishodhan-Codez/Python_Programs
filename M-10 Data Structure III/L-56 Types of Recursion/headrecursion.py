def headrec(n,num) :
    if n > num :
        return
    headrec(n+1,num)
    print(n)
n = int(input("Enter a number to print for n until : "))
headrec(1,n)