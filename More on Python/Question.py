# Find the sum of the cube of the odd digits in a number - p
p = input("Enter a number : ")
sum = 0
for i in p :
    a = int(i)%2
    if a != 0 :
        sum += (int(i))**3
print(f"The sum of the cube of the odd digits in the number - {p} is {sum}")
