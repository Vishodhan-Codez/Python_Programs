n,c = int(input("Enter the length of the range : ")),[]
for i in range(0,n) :
    c.append(i)
result = [i*i for i in c ]
print(c)
print(result)