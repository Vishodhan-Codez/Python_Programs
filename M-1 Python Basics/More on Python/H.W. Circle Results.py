class Circles:
    def __init__(self, r):
        self.r = r
        self.p = 3.14159265359
    def pm(self):
        self.peri = 2 * self.p * self.r
        return self.peri

    def ar(self):
        self.area = self.p * self.r ** 2
        return self.area
radius = int(input("Enter the radius of the circle: "))
obj1 = Circles(radius)
print(f"The perimeter of the circle is {obj1.pm()} and the area is {obj1.ar()}.")