def palindrome(a,i=1) :
    if i==len(a)-1 :
        return "Yes the list is palindrome"
    
    if a[i-1] == a[-i] :
        return palindrome(a,i+1)
    return "The list is not palindrome"
li= [1,43,6,0,6,43,1]
li2 =[1,3,4]
print(li)
print(palindrome(li))
print("\n",li2)
print(palindrome(li2))