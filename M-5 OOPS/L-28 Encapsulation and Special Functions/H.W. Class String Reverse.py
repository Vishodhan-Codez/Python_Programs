class Rs:
    def __init__(self, strinput):
        self.str1 = strinput
    
    def rev(self):
        word = self.str1.split()
        rev = ""
        for i in word[::-1]:
            rev += i + " "
        print(rev )

foop = Rs(input("Enter a string : "))
foop.rev()