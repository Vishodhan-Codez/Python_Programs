def oddevn(a,lena,leng= 1,e=0,maxl=0): #e=0 means even
    if a[0]%2 != 0  : e =1 #odd
    for i in range(1,lena):
        if (a[i]%2==0): 
            if e == 1 :leng+= 1 
            else : leng = 1
            e = 0           
        else:
            if e==0 : leng+= 1 
            else : leng= 1
            e = 1
        if leng > maxl :
                maxl = leng
    print(f"The maximum length of alternate odd~evens in\n{a} \nis {maxl}")
a = eval(input("Enter a list with +ve elements in '[]' :\n"))
oddevn(a,len(a))
        
    