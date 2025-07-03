def n(og,a) :
    if a == 1 : #set up
        pod = 1
    a += 1
    pod *= a #function
    if a == og : #terminate
        print(og,"! = ",pod)
        exit()
    n(og,a)
n(int(input("Enter the nos to factorioalise ")),1)
         

