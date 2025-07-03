wrd = input("Enter a word or sentence : ")
chrc = input("Enter a charcter to check for how many times it is repeated : ")
resul = 0 
i = 0
while i < len(wrd) :
    if chrc == wrd[i] :
        resul += 1 
    i += 1
print("There are ",resul," number of ",chrc," in ",wrd)