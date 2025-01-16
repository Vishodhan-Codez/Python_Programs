num = int(input("Enter a number to check how many digits are there : "))
n = num
count = 0
while num > 0:
    num = num//10
    count += 1
print("The number of digit(s) in ",n," is/are ", count," .")
