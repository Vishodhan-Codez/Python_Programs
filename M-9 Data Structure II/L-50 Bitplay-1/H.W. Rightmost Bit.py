n = int(input("Enter a number: "))
if n == 0:
    print("No set bits found (number is 0).")
else:
    position = 1
    while (n & 1) == 0:
        n >>= 1
        position += 1
    print(f"The rightmost set bit is at the {position}th position")



"""One more method"""
#n = bin(int(input("Enter a number: ")))[2:]
#n = reversed(n) 
#iterations = 0
#for i in n:
#    iterations += 1
#    if i == '1':
#        print(f"The rightmost set bit is at the {iterations}th position")
#        break
