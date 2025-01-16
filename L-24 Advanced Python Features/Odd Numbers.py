n = int(input("Enter a number : "))
c = []
for i in range(n) :
    c.append(i)
result = [i for i in c if not(i%2 == 0 )]
print(result)