def maxi(l,max1 = -99999999999) :
    for i in l :
        if i > max1 :
            max1 = i 
    print("The greatest number is",max1)
    return
def mini(l,min1 = 99999999999) :
    for i in l :
        if i < min1 :
            min1 = i 
    print("The smallest number is",min1)
    return
l = eval(input("Enter a list in '[]' - \n"))
maxi(l)
mini(l)