from abc import ABC,abstractmethod
class ABCD(ABC) :
    def display(self,x) :
        print("Hello I am ",x)
    @abstractmethod
    def t1(self) :
        print(" I am absract !")
class Child(ABCD):
    def t1(self) :
        print(" I am absract 2 !")
eg1 = Child()
eg1.t1()
eg1.display("a screen")
    