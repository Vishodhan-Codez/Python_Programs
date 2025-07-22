def sumofdig(n,sum=0) :
    if len(str(n)) == 1 :
        return sum+n
    sum += n%10
    return sumofdig(n//10,sum)
print("The sum of the digits in the number is - ",sumofdig(int(input("Enter a number to calculate the sum : "))))