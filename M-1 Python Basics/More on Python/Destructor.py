class Employer :
    def __init__(self) :
        print("Employee 1 created")
    def __del__(self): #desturctor
        print("Employee 1 deleted")
obj1 = Employer()
del obj1
#print(obj) => Name Error
