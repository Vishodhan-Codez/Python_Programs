n = int(input("Enter a number : "))
result,temp = "",n
while temp > 0 :
    digit = temp%10
    result += str(digit)
    temp = temp//10
if len(str(n)) == 1 :
    print(f"{n} is a one-digit number")
elif int(result) == n :
    print(f"{n} is a palindrome")
else :
    print(f"{n} is not a palindrome")
