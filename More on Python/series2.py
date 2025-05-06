# 1^2 + 3^2 + 5^2 ... n
n = int(input("Enter the length of the series : "))
sum = 0
n1 = 1
for i in range(1,n+1):
    sum += n1**2
    n1 += 2
print(f"The sum of the series is {sum}")