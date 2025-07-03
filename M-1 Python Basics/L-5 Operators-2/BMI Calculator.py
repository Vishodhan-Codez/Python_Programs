h = float(input("Enter your height in cm : "))
w = float(input("Enter your weight in kg : "))
bmi = w /((h/100)**2)
print("Your BMI is ",bmi," .")
if bmi <= 18.4 :
  print("You are underweight !")
elif bmi <= 24.9 :
  print("Your BMI is Normal .")
elif bmi <= (24.9 + 5) :
  print("You are overweight . ")
elif bmi <= (24.9+10) :
  print("You are severly overweight !!")
elif bmi <= (24.9+15) :
  print("You are obese !!!")
else :
  print("YOU ARE SEVERLY OBESE !!!!")