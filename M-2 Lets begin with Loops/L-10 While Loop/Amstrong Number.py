num = int(input("Enter a 3-digit number to check whether it is Amstrong or not : "))
if num >= 100 and num < 1000 :
    temp = num 
    sum = 0 
    while num > 0 :
        n1 = num%10
        sum += (n1**3)
        num = num//10
    if temp == sum :
        print("The number is Amstrong !!")
    else :
        print("The number is not Armstrong.")
else :
    print("Enter a correct number between 100 to 999")

    