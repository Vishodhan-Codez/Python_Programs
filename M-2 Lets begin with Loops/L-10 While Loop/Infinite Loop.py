print("This is an infinite number simulator")
n,i = True,1
while n :
    print(i)
    i += 1
    if i == 1000 :
        ans = input("Do you wish to continue ?\n Enter 'No' or 'Yes' ")
        if ans == "No" or ans == "no" or ans == "False" :
            n = False
            print("Game Over")
        else :
            print("Continueing")

