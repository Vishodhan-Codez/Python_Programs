def arm_num(a) :
   num = a 
   sum = 0
   while a > 0 :
     r=a%10
     sum += (r**3)
     a //= 10
   if num == sum :
      return ("The number is Armstrong ")
   else :
      return("The number isn't Armstong ") 
j = int(input("Enter a number to check for Armstrong or not :"))
print(arm_num(j))