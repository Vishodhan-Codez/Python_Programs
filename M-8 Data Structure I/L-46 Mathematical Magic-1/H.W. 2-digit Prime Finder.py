import random
numbers = []
primes = []

for _ in range(1, random.randint(5, 25)):
    nos = random.randint(1, 1001)
    numbers.append(nos)

for num in numbers:
    if 10 <= num <= 99:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

print(f"The 2-digit Prime numbers in the numbers - {numbers} are :\n{primes}")
