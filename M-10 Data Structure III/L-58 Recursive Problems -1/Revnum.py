def revnum(n,rev=0) :
    if n == 0 :
        return rev
    return revnum(n//10,rev*10+ n%10)
print("The Reversed Number - ",revnum(int(input("Enter a number : "))))
