def revstring(n) :
    if len(n) == 1 :
        return n[0]
    s = n[0]
    return revstring(n[1:])+s
print('The reversed string is - "',revstring(input("Enter a string to reverse : ")),'"')
