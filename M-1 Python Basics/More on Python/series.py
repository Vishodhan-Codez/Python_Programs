# 1+4+7.....n , find sum 
n = int(input("Enter the length of the series : "))
start = 1
sum = 0
for _ in range(1,n+1) :
    sum += start
    start += 3
print(f"The sum of the series is {sum}")