print("Enter your marks out of 80")
sub_1 = float(input("Enter your marks in English : "))
sub_2 = float(input("Enter your marks in 2nd Language : "))
sub_3 = float(input("Enter your marks in Mathematics : "))
sub_4 = float(input("Enter your marks in Science : "))
sub_5 = float(input("Enter your marks in Social Science : "))
avg = (sub_1+sub_2+sub_3+sub_4+sub_5)/5
percent = ((sub_1+sub_2+sub_3+sub_4+sub_5)/(80*5))*100
print("Your average is ",avg,"\nYour total percentage is ",percent,"%")