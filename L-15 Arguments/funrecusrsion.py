def fun(n) :
    if n == 1 or n == 0 :
        return 1 
    else :
        return n*fun(n-1)
num = int(input("Enter a number to get the factorial of : "))
print(f"{num}! is {fun(num)}")