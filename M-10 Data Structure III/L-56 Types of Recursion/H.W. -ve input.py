def negative() :
    n = int(input("Enter a number : "))
    if n < 0 :
        print("Number -ve")
        return
    elif n == 0 :
        print("Zero 0 ")
    print("Number +ve")
    negative()
negative()
    
    