tup1=(1,2,3,4,5,6)
for i in tup1 :
    print(f"The square of {i} in {tup1} is {i**2}")
def square1(tup1) :
    return tup1**2
print(list(map(square1,tup1)))

