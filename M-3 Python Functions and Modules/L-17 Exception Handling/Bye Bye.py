n = True
while n :
    try :
        n1 = int(input("Enter a number : "))
        while (n1%2)==0:
            print("bye")
        else :
            break
    except :
        print(ValueError)
