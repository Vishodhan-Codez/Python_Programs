sample1 = 45
print("Before Converting : ")
print(sample1,type(sample1))
sample1 = float(sample1)
print("After Converting : ")
print(sample1,type(sample1),"\n")

string1 = "45.8"
print(string1,type(string1))
string1 = float(string1)
print(string1,type(string1))
string1 = int(string1)
print(string1,type(string1),"\n")

number1 = 45.676
print(number1,type(number1))
number1 = int(number1)
print(number1,type(number1),"\n")

# HAD : ₹100 , Discount : 18% , Payable amount ;?

in_a = 100
b = in_a*0.18
cost = in_a-b
print("You have to pay :Rs.",cost)

# find why it is float (answer)