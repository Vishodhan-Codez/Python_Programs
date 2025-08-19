n = eval(input("Enter a list : "))
mx = -1
for i in n :
    if len(str(i)) > mx :
        mx = len(str(i))
print("The maximum no.of digits in a no. in the list is",mx)