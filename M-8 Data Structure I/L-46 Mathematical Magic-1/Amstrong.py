n = int(input("Enter a number : "))
digits = len(str(n))
result = 0
temp = n
while temp > 0 :
    digit = temp%10
    result += digit**digits
    temp = temp//10
if result == n :
    print(f"{n} is a armstrong number.")
elif n < 0 :
    print(f"{n} is negative , enter a positive number.")
else :
    print(f"{n} is not a armstrong number.")