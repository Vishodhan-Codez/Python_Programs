def terminat(n,t) :
    if n>t :
        return
    print(n)
    terminat(n+1,t)
terminat(int(input("enter the value of n : ")),int(input("enter the terminating value :")))