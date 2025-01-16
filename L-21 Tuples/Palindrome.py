paltuple= (1,2,3,2,1)
''' for i in paltuple :
    if paltuple[o] == paltuple[q] :
        o += 1 
        q -= 1
        continue 
    else :
        print("It is not a Palindrome")
        break '''
def palindrome(paltuple) :
    o = 0 
    q = len(paltuple)-1
    while o < q :
        if paltuple[o] != paltuple[q] :
            return False
        o += 1 
        q -= 1 
    return True
if palindrome(paltuple):
    print("The number is Palindrome")
else :
    print("The number is not Palindrome")