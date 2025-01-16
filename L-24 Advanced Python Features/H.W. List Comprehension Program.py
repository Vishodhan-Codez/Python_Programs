n = int(input("Enter a number : "))
o = []
for i in range(n) :
    o.append(i)
result = [i for i in o if not(i%2 == 0 )]
print(result)

#fru = ["apple", "orange", "banana"]
#result = [z for z in fru capitalize(z)]
#print("The capitlazised list is ",result)
# this is not working
#so
fru = ["apple", "orange", "banana"]
result = []
for z in fru:
    result.append(z.capitalize())
print("The list is ",fru)
print("The capitalized list is", result)

