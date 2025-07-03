num = int(input("Enter the number of numbers you wish to enter : "))
n = []
o1e = []
for i in range(0,num,1) :
    n1 = int(input(f"Enter the number : "))
    if n1%2 == 0 :
        o2e= "Even"
    else :
        o2e = "Odd"
    o1e.append(o2e)
    n.append(n1)
print(n)
print(o1e)
    