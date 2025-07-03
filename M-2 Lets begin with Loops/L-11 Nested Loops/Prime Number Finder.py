lr = int(input("Enter the range between what prime numbers have to be found\nEnter the lower range : "))
hr = int(input("Enter the higher range : "))
for i in range(lr,(hr+1)) :
    if i > 1 :
        for j in range(2,i) :
            if i%j == 0 :
                break 
        else :
            print(i)