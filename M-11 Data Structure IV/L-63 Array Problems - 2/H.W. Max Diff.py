def maxdiff(a,alen):
    mx,mn = -999999999,999999999
    for i in range(alen) :
        if a[i] > mx :
            mx = a[i]
        if a[i] < mn :
            mn = a[i]
    print(mx-mn)
a = eval(input("Enter a list : "))
print("The maximum diffrence in the lists is",end=" ")
maxdiff(a,len(a))