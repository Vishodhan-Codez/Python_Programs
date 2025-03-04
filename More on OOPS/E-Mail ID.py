eid = input("Enter the email ID : ")
sum = 0
for i in eid :
    if i.isdigit() :
        sum += int(i)
print(sum)

