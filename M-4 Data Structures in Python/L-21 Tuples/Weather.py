forecast = (1,0,0,0,1,1,0)
''' count1 = 0
for i in forecast :
    if i == 1 :
        count1 += 1 
    else :
        count1 -= 1 
if count1 < 0 :
    print("The weather is sunny !! ")
else :
    print("The weather is rainy ") '''
sunny = forecast.count(0) 
rainy = forecast.count(1)
if sunny > rainy :
    print("The weather is sunny !! ")
else :
    print("The weather is rainy ") 

