def streak0(a,b):
    c=a.count(0)
    for i in a :
        if i != 0 :
            b.append(i)
    else:
        for _ in range(c):
            b.append(0)
    print(f"The new list is {b}")
arr = [1,2,0,-9,8,-67,5,4,2,-36,0,5467,-54,7,45,0,56,0,-56,-7,0,7,0,-87,56]
streak0(arr,b=[])