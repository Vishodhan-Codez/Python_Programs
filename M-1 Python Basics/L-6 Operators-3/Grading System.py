print("Enter your subject amrks out of 100 marks : ")
eng = float(input("Enter your marks in English : "))
sans = float(input("Enter your marks in 2nd Language : "))
math = float(input("Enter your marks in Mathematics : "))
sci = float(input("Enter your marks in Science : "))
sst = float(input("Enter your marks in Social Science : "))
print("Your avarage is",(eng+sans+math+sci+sst)/5,"%",sep=" ")
print("Your grade is ")
if ((eng+sans+math+sci+sst)/5) >= 90 :
    print("A1 - Oustanding Performance !! ")
elif ((eng+sans+math+sci+sst)/5) >= 84 :
    print("A2 - Excellent Performance , A little hardwork can get you better !")
elif ((eng+sans+math+sci+sst)/5) >= 76 :
    print("B1 - Above Average , Concentrate on Studying and you will go higher ! ")
elif ((eng+sans+math+sci+sst)/5) >= 68 :
    print("B2 - Average , Work Harder and you will fly !")
elif ((eng+sans+math+sci+sst)/5) >= 59 :
    print("C - Below Average ,More effort needs to be put in studying and you will stand out :)")
elif ((eng+sans+math+sci+sst)/5) >= 49 :
    print("D - Need a scoop of Imporvement , Need a lot of hard work and effort to get higher !")
else :
    print("F - Fail ,Need to Study effectivly :(")
