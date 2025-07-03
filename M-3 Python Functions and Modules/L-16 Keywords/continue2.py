word = input("Enter a word : ")
word = word.upper()
word1 = []
for i in word :
    if i == 'A' or i == 'E' or i == 'O' or i == 'U' or i == 'I' :
        continue
    else:
        word1.append(i)
print(word1)
