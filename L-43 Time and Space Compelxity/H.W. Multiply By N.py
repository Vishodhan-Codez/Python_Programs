m = int(input("Enter a number : "))
n = int(input("Enter another number : "))
def method1(a,b) : # for 1 iteration
    return a*b
def method2(a,b) : # for n interations
    pro = 0
    for _ in range(b) :
        pro += a
    return pro
print(f"The product of {m} and {n} by\nMethod 1 is {method1(m,n)}\nMethod 2 is {method2(m,n)}")
