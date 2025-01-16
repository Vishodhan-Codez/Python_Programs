# 1(cube)+4(cube)+7(cube)+10(cube)....n(cube)
n,sum,b = int(input("Enter a number to add numbers up to : ")),0,1
for i in range(1,n+1,1) :
    sum += (b**3)
    b += 3
print(f"The sum of number is {sum}")