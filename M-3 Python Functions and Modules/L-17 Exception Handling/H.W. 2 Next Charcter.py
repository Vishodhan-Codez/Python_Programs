# You have to convert a word with letters to the next letter 
# eg : CAT => DBU , HOP => IPQ
word = input("Enter a word: ")
result = ""
for char in word:
    if char.isalpha():
        result += chr(ord(char) + 1)
    else:
        result += char

print("Transformed word:", result)