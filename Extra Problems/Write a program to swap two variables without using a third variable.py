# Write a program to swap two variables without using a third variable
a = int(input("Enter a number : ")) # 5
b = int(input("Enter a second number : ")) #3
a += b # 5 + 3 = 8 = a
b = a-b #8-3=  5 = b
a -= b # 8 - 5 = 3 = a
print(f"The first number is {a} now and the second number is {b}.")