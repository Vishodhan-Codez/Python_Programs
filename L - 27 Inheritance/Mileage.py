class Vechile :
    def __init__(self,name,speed,mil) :
        self.name = name
        self.speed = speed
        self.mil = mil
class Bus(Vechile) :
    pass
obj1 = Bus("School Volvo",180,22) 
print(f"Name : {obj1.name}\nSpeed : {obj1.speed} km/hr \nMileage : {obj1.mil} km/hr")