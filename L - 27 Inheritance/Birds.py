class Bird :
    def __init__(self,name,lfsp) :
        self.name = name
        self.lfspan = lfsp
    def display(self) :
        print("Name : ",self.name)
        print("The lifespan of the bird is : ",self.lfspan)
    def msg(self) :
        print("Birds are wonderful animals !! ")
class Species(Bird) :
    def __init__(self,name,lfspan,species) :
        self.sp = species
        super().__init__(name,lfspan) #syntax is super().__init__([name of importing variables])
    def display2(self) :
        print("The species of the bird is ",self.sp)
obj1 = Species("Macaw","14 years","Macawius indicus")
obj1.display(),obj1.display2(),obj1.msg()
