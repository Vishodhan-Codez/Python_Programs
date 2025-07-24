def paren(s,l,r,p,n):
    if p == 2*n :
        for ss in s :
            print(ss,end=" ")
        print("\n")
        return 
    if l>r : 
        s[p] = "}"
        paren(s,l,r+1,p+1,n)
    if l<n :
        s[p] = "{"
        paren(s,l+1,r,p+1,n)
n = int(input("Enter the no.of pairs of parentheses : '{-}' -\n"))
s = [""]*n*2
paren(s,0,0,0,n)