n = [1,2,3,4,5]
def sq(num):
    return num*num
result = map(sq,n)
print("The squares of the number are : ")
print(list(result))

#2 
o = [5,6,8,9]
p = [1,2,3,4]
result = map(lambda x,y : x+y , o,p) 
print("The result is : ")
print(list(result))
