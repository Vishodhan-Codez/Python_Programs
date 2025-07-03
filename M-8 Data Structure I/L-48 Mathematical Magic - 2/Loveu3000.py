nos = int(input("Enter the range to which you want to find prime numbers till :\n"))
primes = []
for i in range(2,nos+1) :
    factors = True
    for j in range(2,i) :
        if i%j == 0 :
            factors = False
            break
        else :
            pass
    if factors == True :
        primes.append(i)
print(f"The list of primes up till {nos} is/are :\n{primes}")

