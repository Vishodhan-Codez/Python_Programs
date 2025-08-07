def great2(l,b=-99999999999) : 
    for i in l :
        if i > b and i != max(l) :
            b = i
    print("The second largest number in the value(s) is",b)
l = eval(input("Enter a list in '[]' - \n"))
great2(l)