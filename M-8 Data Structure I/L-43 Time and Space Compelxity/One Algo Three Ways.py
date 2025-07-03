n = int(input("Enter the no.of numbers you wish to add : "))
def sum1(nos) :
    return (nos*(nos+1))/2
def sum2(nos) :
    sum = 0
    for i in range(nos+1) :
        sum += i
    return sum
def sum3(nos) :
    sum = 0
    for i in range(nos+1) :
        for j in range(i) :
            sum+= 1
            print(j)
    return sum
a = sum1(n)
b = sum2(n)
c = sum3(n)
print(f"The sum from \nMethod 1 is {a}\nMethod 2 is {b}\nMethod 3 is {c}")
# Iterations
# The no. of iterations in Method-1 is 1 
# This is because the method is executed only one time 
# EG : input(4) => 4*5/2 => 20/2 => 10 
# The no. of iterations in Method-2 is 'nos'
# This is beacuse the loop in the method is executed 'nos' times
# EG : input(4) => in [1,2,3,4] 
#      0+1 = 1 (1)
#      1+2 = 3 (2)
#      3+3 = 6 (3)
#      6+4 = 10 (4)
# The no.of iterations in Method-3 is 10 for input(4) as two loops are involved as the iterations are
# guided by the outer and inner loop
# EG : input(4) => 1 + (1+1) + (1+1+1) + (1+1+1+1) = 10
