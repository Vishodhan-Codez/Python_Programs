tran = int(input("Enter the mode of transport \nFor Car ,Enter 1 and for Bike ,Enter 2 :"))
if tran == 1 :
    type = int(input("You have choosen 'Car' , choose your preferred car \n1. Audi\n2. Toyota\n3.Volksvagan\n4.Ferrari\n For your brand type the serial number"))
    if type == 1:
        print("Enjoy the progressive design and precisely sharp looks of the Audi A4. Book a test drive. Drive the statement of sportiness and turn heads wherever you go with the Audi")
    elif type == 2:
        print("Enjoy your ride in the Toyota Rumaron ")
    elif type == 3:
        print("Enjoy your ride in the Volksvagan Virtus ,A sedan with a 1.5L TSI EVO engine and a choice between a 6-speed manual or 7-speed DSG transmission ")
    elif type == 4:
        print("Enjoy your super fast ride in Ferrari's SF90 Stradale")
    else :
        print("Enter any number between 1 to 4 ")
        tran = int(input("Enter the mode of transport \nFor Car ,Enter 1 and for Bike ,Enter 2 :"))
if tran == 1 :
    type = int(input("You have choosen 'Car' , choose your preferred car \n1. Audi\n2. Toyota\n3.Volksvagan\n4.Ferrari\n For your brand type the serial number"))
    if type == 1:
        print("Enjoy the progressive design and precisely sharp looks of the Audi A4. Book a test drive. Drive the statement of sportiness and turn heads wherever you go with the Audi")
    elif type == 2:
        print("Enjoy your ride in the Toyota Rumaron ")
    elif type == 3:
        print("Enjoy your ride in the Volksvagan Virtus ,A sedan with a 1.5L TSI EVO engine and a choice between a 6-speed manual or 7-speed DSG transmission ")
    elif type == 4:
        print("Enjoy your super fast ride in Ferrari's SF90 Stradale")
    else :
        print("Enter any number between 1 to 4 ")
elif tran == 2:
    type = int(input("You have choosen 'Bike' , choose your preferred car \n1.Yamaha\n2.Bajaj Auto\n3.Honda\n4.Royal Enfield\n For your brand type the serial number"))
    if type == 1:
        print("Enjoy your ride in the MT 15 V2 ")
    elif type == 2:
        print("Enjoy your ride in the Pulsar N160")
    elif type == 3:
        print("Enjoy your ride in the SP 125")
    elif type == 4:
        print("Enjoy your ride in the Royal Enfield 11")
    else :
        print("Enter any number between 1 to 4 ")  
         
else :
    print("Enter a correct value")