def revgroup(a,lena,n) :
    temp = 0
    while temp < lena :
        start = temp
        end = min(temp+n-1 , lena-1 )
        while start < end :
            a[start],a[end] = a[end],a[start]
            start += 1 
            end -= 1
        temp += n 

a = eval(input('Enter a list -  '))
lena = len(a)
n = int(input("Enter the no. of terms in the series - "))
revgroup(a,lena,n)
print(a)