def kadane(a) :
    n = len(a)
    max = cmax = 0
    for i in range(n) :
        cmax += a[i] 
        if cmax < 0 :
            cmax = 0
        if max < cmax :
            max = cmax
    return max
def maximumsubarray(a,n) :
    mxk = kadane(a)
    mnk = 0
    for i in range(n) :
        mnk += a[i]
        a[i] = -a[i]
    mnk += kadane(a)
    if mxk >= mnk :
        return mxk
    else :
        return mnk
a = [1,2,3,-6,-8,5,-4,-31,-94,-345]
print("The maximum subarray sum is",maximumsubarray(a,len(a)))