class myclass :
    __privvar = 50
    def __privmethod(self) :
        print("Hello ! I am a private method")
    def publicmethod(self) :
        print("Hello the value of the private variable is : ",myclass.__privvar)
foop = myclass()
foop.publicmethod()
foop.__privatemethod() #error