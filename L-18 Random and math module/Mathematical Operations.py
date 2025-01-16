import math
n = float(input("Enter a number : "))
print("The rounded number is ",math.floor(n))
print("The upper rounded number is ",math.ceil(n))
print("The absolute value is ",math.fabs(n))
n1 = float(input("Enter another number : "))
print("The numbers with switched signs are ",math.copysign(n,n1))
print("The HCF of the two numbers is ",math.gcd(int(n),int(n1)))



