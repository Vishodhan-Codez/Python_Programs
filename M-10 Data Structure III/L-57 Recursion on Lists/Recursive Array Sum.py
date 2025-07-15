def arraysum(a):
    if len(a) == 1:
        return a[0]
    return a[0]+(arraysum(a[1:]))
a1 = [1,2,4,6,8,10]
print("The sum of the digits in the array is \n",arraysum(a1))
