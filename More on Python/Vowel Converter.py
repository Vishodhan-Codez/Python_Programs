#Vishodhan => Vjshpdhbn
chrs = input("Enter a word : ")
final = ''
chrs = chrs.lower()
for i in chrs :
    if i == "a" :
        final += "b"
    elif i == "e" :
        final += "f"
    elif i == "i" :
        final += "j"
    elif i == "o" :
        final += "p"
    elif i == "u" :
        final += "v"
    else :
        final += i     
final.capitalize()   
print(final)

    