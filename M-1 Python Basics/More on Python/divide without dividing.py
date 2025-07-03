def divide1(dividend,divisor) :
    if divisor == 0 :
        print("Not Defined")
        exit()
    rem = dividend
    q = 0
    while (rem) :
        if rem != 0 :
            q += 1 
        rem -= divisor 
    return q  
print(f"The quotient is {divide1(int(input("Enter the dividend : ")),int(input("Enter the divisor : ")))}")