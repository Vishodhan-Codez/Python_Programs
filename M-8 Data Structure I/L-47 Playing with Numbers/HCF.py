n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
hcf = [1]
if m > n :
    for i in range(2,m) :
        if m%i == 0 and n%i == 0:
            hcf.append(i)
elif n > m :
    for i in range(2,n) :
        if m%i == 0 and n%i == 0:
            hcf.append(i)
else :
    print(f"The HCF of {m} and {n} is the number itself - {m}")
print(f"The HCF of {m} and {n} is {hcf[-1]}")      