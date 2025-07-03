bin = str(input("Enter a binary number in 1's and 0's : "))
dec = 0
for i in range(len(bin)):
    n = 2**i
    dec += int(bin[-1 - i])*n #[-1-i] gets from backside of string 0
print(dec)
