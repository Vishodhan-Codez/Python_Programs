def revarray(l,leng) :
    for i in range(leng//2) : 
        l[i],l[-(i+1)] = l[-(i+1)],l[i] # 1st lement => last element , last element => first element
    print("The reversed list is",l)
m = eval(input("Enter a list in '[]' - \n"))
revarray(m,len(m))