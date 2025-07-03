n = int(input("Enter a value of 'n' : "))
dict = {}
sum1 = 0 
for i in range(n):
    dict.update({int(i):int((i**2))})
print(dict)
for j in dict.values():
    sum1 += j
print(sum1," is the sum of all values in ",dict)
s = int(input("Enter a value to search : "))
list1 = list(dict.keys())
list2 = list(dict.values())
print(f"{s} is repeated {(list1.count(n))+(list2.count(n))} time(s)")


