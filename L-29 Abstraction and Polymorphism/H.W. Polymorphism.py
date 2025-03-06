class bmw():
    def fuel_type(self):
        print("BMW cars use Petrol as Fuel ")
    def max_speed(self) :
        print("BMW's max speed is 250 km/hr")
class fer():
    def fuel_type(self):
        print("Ferrari's cars use Diesel as Fuel ")
    def max_speed(self) :
        print("Ferrari's max speed is 290 km/hr")
obj1,obj2 = bmw(),fer()
for i in (obj1,obj2):
    i.fuel_type()
    i.max_speed()