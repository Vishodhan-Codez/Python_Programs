def leader(li) :
    lead = li[len(li)-1]
    for i in range(len(li)-2,-1,-1) : #to reach one beyond 0
        if li[i] > lead :
            print("The new leader is",li[i])
            lead = li[i]
    print("\n\nThe FINAL leader is",lead)
a = eval(input('Enter a list -  '))
leader(a)
