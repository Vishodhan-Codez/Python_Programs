n = int(input("Enter a number : "))
fact = 2
factors = [1,n]
for i in range(2,n) :
    if n%i == 0 :
        fact += 1
        factors.append(i)
if fact == 2 :
    print(f"{n} is a prime number !")
print(f"{n} has {fact} factors\nThe factors of {n} are {factors}")