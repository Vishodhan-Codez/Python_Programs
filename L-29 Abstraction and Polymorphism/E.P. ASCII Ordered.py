x = input("Enter a ASCII Value : ")
li,a =[],""
for i in x:
    li.append(ord(i))
li.sort()
for i in (li) :
    a += "".join(chr(i))
print(a,"is the characters arranged")