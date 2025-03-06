from abc import ABC,abstractmethod
class Animals(ABC) :
    def move(self) :
        pass
class human(Animals):
    def move(self) :
        print("The human moves with two legs")
class dog(Animals):
    def move(self) :
        print("The dog moves with four legs very fast")
class crow(Animals) :
    def move(self) :
        print("The crow moves with its wings by flying around")
obj1 = human()
obj1.move()
obj2 = dog()
obj2.move()
obj3 = crow()
obj3.move()