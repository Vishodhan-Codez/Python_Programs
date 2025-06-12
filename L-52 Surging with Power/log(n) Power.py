def timecomplex(a,b) :
    result =1
    while b > 0 :
        if b%2 == 0 :
            a = a**2
            b >>= 1 
        else :
            result = result * a
            b -= 1 
    return result
print(timecomplex(int(input('Enter a number :')),int(input('Enter another number :'))))