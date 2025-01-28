# Change Capital Letter to Small Letter and Small Letter to Capital Letters
#cAt => CaT using isupper() and islower()
strig = input("Enter a word : ")
sum = ""
for i in strig :
    if i.islower() :
        sum += i.upper()
    elif i.isupper() :
        sum += i.lower()
    else :
        print("Invalid Input !!")
        exit()
print("The converted word is ",sum)