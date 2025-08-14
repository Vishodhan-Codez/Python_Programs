def rotate1(a,n,siz):
    for _ in range(n) :
        rotate2(a,siz)
def rotate2(a,siz) :
    temp = a[0]
    for i in range(siz-1):
        a[i] = a[i+1]
    a[siz-1] = temp
def pri(a) :
    for i in a :
        print(i,end=" , ")
    print("|")
a = eval(input('Enter a list -  '))
lena = len(a)
n = int(input("Enter the no. of terms in the series - "))
pri(a)
rotate1(a,n,lena)
print()
pri(a)


