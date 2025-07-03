a = input("Enter a word : ")
a = a.upper()
for i in a :
    if i == 'A' or i == 'E' or i == 'O' or i == 'U' or i == 'I':
        print("A is found .")
        break
    else :
        print("A is not found .")