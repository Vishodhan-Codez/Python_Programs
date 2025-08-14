def missing(a,l) : 
    for i in range(1,l+1) :
        if a[i-1] != i :
            print("The missing value is",i)
            exit()
    print("The missing value is out of bounds",f"\nOR\nThe number is {a[-1]+1}")

#making the list
n = int(input("Enter the range till which the list is to be printed - "))
li = []
for i in range(1,n+1) :
    li.append(i)
m = int(input("Enter the missing element - "))
li.remove(m)
del m 
print("The list is - \n",li)
lenli = len(li)
missing(li,lenli)

