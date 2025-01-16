try :
    n1,n2 = eval(input("Enter two number seprated by a comma "))
    result = n1/n2
    print("The answer is ",result)
except ZeroDivisionError as zde :
    print(zde)
except :
    print("Invalid Input")
else :
    print("No Error")
finally :
    print("Program ended")

