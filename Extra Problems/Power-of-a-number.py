def powerofanos(man,exp):
    if exp == 0 :
        return 1 
    return powerofanos(man,(exp-1))*man
print("The answer is",powerofanos(int(input("Enter the mantissa : ")),int(input("Enter the exponent : "))))