# a ^a = 0
# a ^ 0 = a 
def Oneoddoccuringnumber(arr) :
    res = 0
    for element in arr :
        res = res ^ element
    return res
array = []
for i in range(1,(int(input("Enter a the lenght of the array : "))+1)) :
    print("Enter the",i,"th element : ")
    array.append(int(input()))
print(Oneoddoccuringnumber(array))