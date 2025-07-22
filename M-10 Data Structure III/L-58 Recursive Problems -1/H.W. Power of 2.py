def p2(n):
    if  n == 1 :
        return True
    if n%2 == 0 :
        return p2(n/2)
    return False
num = int(input("Enter a number: "))
if p2(num):
    print(f"{num} is a power of 2.")
else:
    print(f"{num} is NOT a power of 2.")