#loop 1 -10 , skip 3,5,8
for i in range(1,11,1) :
    if i == 3 or i == 5 or i == 8 :
        continue
    else :
        print(i)