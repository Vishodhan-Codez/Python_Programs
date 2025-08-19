def profit(li,leng):
    p = 0
    for i in range(1,leng) :
        if li[i] > li[i-1] :
            p += li[i] - li[i-1]
    return p
a = [14,2,4,10]
l = len(a)
print(profit(a,l))
