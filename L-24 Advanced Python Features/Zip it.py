s1 = {2,3,4}
s2 = {"a","b","n"}
res = zip(s1,s2)
print(list(res)," is the result")

stu = ["Raju","Aditi","Nikhil"]
ron = [23,4,24]
for x,y in zip(stu,ron[::-1]) :
    print(x,y)

stocks = ["Aditya Birla Co","Tata Motors","Coal India"]
price = [4365.66 , 2835.13 , 1393.99 ]
res = {stocks : price for stocks , price in zip(stocks[::-1],price)}
print(res)