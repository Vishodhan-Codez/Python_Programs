#Sieve of Erithosenes
def Sieveoferithosenes(num) :
    primes = [True for _ in range(0,num+1)]
    p = 2
    while (p**2 <= num) :
        if primes[p] == True :
            for i in range(p**2,num+1,p) :
                primes[i] = False
        p+= 1
    for j in range(2,num+1) :
        if primes[j] == True :
            print(j)
n = int(input("\nEnter a number to check for primes until : \n"))
Sieveoferithosenes(n)