#no loops
a = [1,2]
a1 = [5,0]
def hello(a) :
    return a**2
b = map(hello,a) # map(function_name,list)
print(list(b))

def even(b):
    if b%2 == 0 :
        return True
    else :
        return False
c = map(even,a)
print(list(c))

#zip zips two data types of same length and returns zipped object
def add(a,b):
    return a+b
print(list(map(add,a,a1)))
print(list(map(lambda x,y: x+y,a,a1)))

