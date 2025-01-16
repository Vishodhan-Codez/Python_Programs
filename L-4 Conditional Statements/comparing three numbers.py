n1 = float(input("Enter the first number : "))
n2 = float(input("Enter the second number : "))
n3 = float(input("Enter the third number : "))
big_num = 0
if n1 > n2 and n1 > n3 :
  big_num = n1
elif n2 > n1 and n2 > n3 :
  big_num = n2
else :
  big_num = n3 
print("The greatest number is ",big_num)