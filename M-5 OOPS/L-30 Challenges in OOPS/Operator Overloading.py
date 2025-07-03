class fun :
    def __init__(self,a) :
        self.a = a
    def __lt__(self,b) :
        if (self.a < b.a) :
            return "obj1.a is smaller than obj2.b"
        else :
            return "obj1.a is larger than obj2.b"
    def __eq__(self,c) :
        if self.a == c.a :
            return "obj1.a is equal to obj3.c"
        else :
            return "obj1.a is not equal to obj3.c"
obj1 = fun(2)
obj2 = fun(3)
print(obj1 < obj2)
obj3 = fun(4)
print(obj1 == obj3)