#Write a loop to calculate the sum of the digits in a given number from the series
series = "1+2+3+4+5....n"
sum = 0
n = int(input("Enter a number : "))
for i in range(1,n+1) :
    sum += i
print("The sum of the number of digits is ",sum)
