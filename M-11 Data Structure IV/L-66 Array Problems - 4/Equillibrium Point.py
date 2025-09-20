def equisum(a) :
    n = len(li)
    leftsum = rightsum = 0
    for i in range(n):
        leftsum = rightsum = 0
        for j in range(i) :
            leftsum += a[j]
        for j in range(i+1,n) :
            rightsum += a[j]
        if leftsum == rightsum :
            return i
    else : return -1
li = [4,-1,-4,5,0,-2]
print(f"The equidllibrium point is at",equisum(li))