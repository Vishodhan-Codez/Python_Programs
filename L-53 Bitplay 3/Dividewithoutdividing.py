def divide1(dividend,divisor) :
    if divisor == 0 :
        print("Not Defined")
        exit()
    temp = 0
    q = 0
    for i in range(31,-1,-1):
        if (temp + (divisor << i)) <= dividend :
            temp += divisor << i
            q |= 1 << i 
    return q
print(f"The quotient is {divide1(18,6)}")