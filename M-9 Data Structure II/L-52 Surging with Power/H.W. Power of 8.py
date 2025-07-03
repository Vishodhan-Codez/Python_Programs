n = int(input("Enter a number: "))
temp = n
count = 0
if (n & 7) == 0: # n%8
    while ((n & 1) == 0): # check last digit of n is 0
        count += 1
        n >>= 1 #shifting next digit
    if count % 3 == 0: # every power of 8 has the no. of zeroes divisible by 3 
        print(f"{temp} is a power of 8")
        exit()

print(f"{temp} is not a power of 8")

print(bin(int(input("Enter an number : ")))[3:])


""" Normal Code """
#b = int(input("Enter an number : "))
#temp = b
#b = bin(b)[3:]
#noof0 = 0
#if temp%8 == 0 :
#    for i in b:
#        if i != "0" or temp == 0 :
#           print(f"{temp} (1{b}) is not a power of 8")
#           exit()
#        noof0 += 1 
#    if noof0%3 == 0 :
#        print(f"{temp} (1{b}) is a power of 8")
#        exit()
#print(f"{temp} (1{b}) is not a power of 8")

