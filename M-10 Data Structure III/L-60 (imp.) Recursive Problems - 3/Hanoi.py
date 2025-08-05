def Hanoi(n,a,b,c) :
    if n == 1 :
        print("Moving Disc 1 from rod",a,"to rod",b)
        return 
    Hanoi(n-1,a,c,b)
    print("Moving Disc",n,"from rod",a,"to rod",b)
    Hanoi(n-1,c,b,a)
stacks = 3
Hanoi(stacks,"A","C","B")
