# > 50 units - ₹8.00/unit
# < 50 units but > 100 - ₹6.00/unit
# 100 to 150 - ₹4.00/unit 
# 150+ - ₹2.00/unit
Power = float(input("Enter the amount of electricity used (in W/hr) : "))
if Power <= 50 :
    print("The electricity bill is Rs.",7.5*Power)
elif Power > 50 and Power <= 100 :
    print("The electricity bill is Rs.",6*Power)
elif Power > 100 and Power <= 150 :
    print("The electricity bill is Rs.",4.5*Power)
elif Power > 150 :
    print("The electricity bill is Rs.",2.5*Power)
else :
    print("Error , Please input correct values ")
