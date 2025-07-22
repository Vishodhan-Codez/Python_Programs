def powof4(n):
    if n <= 0 :
        return False
    elif n == 1 :
        return True
    elif n%4 == 0 :
        return powof4(n/4)
    else :
        return False
x = int(input("Enter a number : "))
if powof4(x):
    print("{} is a power of 4".format(x))
else :
    print(f"{x} is NOT a power of 4")