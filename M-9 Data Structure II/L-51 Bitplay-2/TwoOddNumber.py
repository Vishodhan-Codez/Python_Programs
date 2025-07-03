size = int(input("Enter the total no. of elements : "))
os1 = size
array = []
while (os1) :
    print("Enter the element :")
    array.append(int(input()))
    os1 -= 1
xor2 = array[0]
x = 0
y = 0
setbit = 0
for i in range(1,len(array)):
    xor2 = xor2 ^ array[i]
setbit = xor2 & ~(xor2 -1)
for i in range(len(array)) :
    if array[i] & setbit :
        x= x^array[i]
    else :
        y = y^array[i]
print("The value of x is",x,"\nThe value of y is",y)

