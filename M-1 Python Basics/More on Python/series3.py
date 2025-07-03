# (x+1)^2 + (3x+5)^6 + ..... n 
# b*3 , c+4 , n*3 
length = int(input("Enter the length of the series : "))
x = int(input("Enter the value of x : "))
sum = 0 
b,c,n = 1,1,2
for i in range(length) :
    sum += ((b*x)+(c))**(n)  #bx^2 + c^2 + 2xc
    b *= 3
    c += 4
    n *= 3
print(f"The value of the series is {sum}")