med_ = input("Do you have any medical issues ?\nEnter 'Y' for yes and 'N' for no :")
if med_ == 'Y' :
    print("You are eligible to take the test")
else :
    att_ = int(input("Enter your attendence in % : "))
    if att_ <= 75 :
        print("You are not eligible to take the test ")
    else :
        print("You are eligible to take the test")