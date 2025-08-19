def matrix(a,b,l) :
    c = [[0,0]]*l
    for i in range(l) :
        for j in range(2) :
            c[i][j] = a[i][j] + b[i][j]
    print(c)
    return
a = eval(input("Enter a list with lists : "))
b = eval(input(f"Enter a list containing {len(a)} lists  : "))
if len(a) != len(b) : 
    exit("!! Please enter equal lists !! ")
matrix(a,b,len(a))
