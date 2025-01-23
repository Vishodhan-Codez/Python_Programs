class IOSString:
    def __init__(self) :
        self.str1 = ""
    def getstr(self) :
        self.str1 = input("Enter a string : ")
    def printstr(self) :
        print(self.str1," => ")
        print(self.str1.upper())
n1 = IOSString()
n1.getstr()
n1.printstr()