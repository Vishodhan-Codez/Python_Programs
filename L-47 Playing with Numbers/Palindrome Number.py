n = int(input("Enter a number : "))
temp = n
rev = 0
while temp > 0 :
    digit = temp%10
    rev = rev*10 + digit
    temp //= 10
if rev == n :
    print(f"{n} is a Palindrome Number !")
else :
    print(f"{n} is not a Palindrome Number")