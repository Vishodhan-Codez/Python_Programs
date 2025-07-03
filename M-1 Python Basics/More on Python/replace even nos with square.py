list1 = eval(input("Enter a list :"))
index = 0
for i in list1 :
    if i%2 == 0 :
        list1.pop(index)
        list1.insert(index,i**2)
    index += 1 
print("The final list is",list1)