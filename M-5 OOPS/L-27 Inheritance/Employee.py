class Person() :
    def __init__(self,name,idn) :
        self.name = name
        self.idn = idn
    def display(self) :
        print(self.name)
        print(self.idn)
class EMP(Person) :
    def __init__(self,name,idn,sal,post) :
        self.sal = sal
        self.post = post 
        Person.__init__(self,name,idn)
obj1 = EMP("Rahul",194853345,50000,'Marketing Officer')
obj1.display()
print(obj1.sal,'\n',obj1.post)
