def wc(temp,mon_no) :
    if temp >= 24 and (mon_no <= 3 and mon_no >= 1):
        print("The season is spring")
    elif temp <= 18 and ((mon_no <= 12 or mon_no == 1)and mon_no >= 9):
        print('The season is winter')
    else :
        print("----")
a = float(input("Enter the Temprature in your region : "))
b = int(input("Enter the month in Number\n eg: Januvary is No.1\n- "))
wc(a,b)
        