nos = int(input("Enter a number to check if prime : "))
factors = [1]
for i in range(2,nos+1) :
    if nos%i == 0 :
        factors.append(i)
if len(factors) == 2 :
    print(f"{nos} is a prime number and it's factors are 1 and itself ({nos})")
else :
    print(f"{nos} is not a prime number\nIt's factors are\n{factors}")