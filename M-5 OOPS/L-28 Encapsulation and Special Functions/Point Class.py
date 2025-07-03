class Point :
    def __init__(self,x,y) :
        self.x1 = x
        self.x2 = y
    def formatt(self) :
        print(f"The point is on \n({self.x1},{self.x2})")
foop = Point(int(input("Enter the value of the x -axis : ")),int(input("Enter the value of the y -axis : ")))
foop.formatt()