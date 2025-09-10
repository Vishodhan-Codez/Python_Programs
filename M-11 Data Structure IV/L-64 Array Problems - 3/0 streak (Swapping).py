def streak0(a,lena) :
    z=nz=0
    while nz != lena :
        if a[nz] != 0 :
            a[nz],a[z]=a[z],a[nz]
            z += 1 
        nz += 1 
    return a
arr = [1,2,0,-9,8,-67,5,4,2,-36,0,5467,-54,7,45,0,56,0,-56,-7,0,7,0,-87,56]
print(streak0(arr,len(arr)))