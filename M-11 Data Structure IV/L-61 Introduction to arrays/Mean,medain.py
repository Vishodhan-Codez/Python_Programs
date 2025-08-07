def meanarr(l,leng) :
    sum = 0
    for i in range(leng) :
        sum += l[i]
    print("The Mean of the value(s) is ",sum/leng)
    return 
def medarr(l,leng) :
    l.sort()
    if leng % 2 != 0 :
        print("The median is ",l[leng//2])
        return
    print("The median of the value(s) is ",((l[leng//2])+(l[leng//2 -1 ]))/2 )  
l = eval(input("Enter a list in '[]' - \n"))
meanarr(l,len(l))
medarr(l,len(l))