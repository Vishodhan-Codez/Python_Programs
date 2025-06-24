list1 = eval(input("Enter a list : "))
x = int(input("Enter an element whos duplicates are to be removed : "))
rc = 0
index = 0
for i in list1 :
    if i == x :
        rc += 1 
        if rc > 1 :
            list1.pop(index)
    index += 1 
print("The final list is \n",list1)