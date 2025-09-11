def maxsubarray(a,lena) :
    max = int("9"*11)*-1
    cmax = 0 
    for i in range(lena) :
        cmax += a[i]
        if cmax > max :
            max = cmax
        if abs(cmax) != cmax:
            cmax = 0 
    return max
a = [1,2,3,-6,-8,5,-4,31,-94,-345]
print(f"The Maximum sum of the subarray in\n{a} is {maxsubarray(a,len(a))}")