n = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
