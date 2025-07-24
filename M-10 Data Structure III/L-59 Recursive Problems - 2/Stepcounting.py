def ways(steps) :
    if steps<0 :
        return 0
    if steps == 0 :
        return 1 
    step1 = 0
    step2 = 0
    if steps >= 2 :
        step2 = ways(steps-2)
    step1 = ways(steps-1)
    return step1+step2
print(f"The no.of ways the steps can be walked is {ways(int(input("Enter the no.of steps : ")))}")