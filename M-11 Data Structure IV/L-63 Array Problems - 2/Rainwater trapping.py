def rainwater(a,alen) :
    left = [0]*alen
    right = [0]*alen
    water = 0 
    left[0] = a[0]
    for i in range(1,alen) :
        left[i] = max(a[i],left[i-1])
    right[alen-1] = a[alen-1]
    for j in range(alen-2,-1,-1) :
        right[j] = max(a[j],right[j+1])
    for i in range(alen) :
        water += min(left[i],right[i]) - a[i]
    return water
a = [1,2,0,1]
print(rainwater(a,len(a)))