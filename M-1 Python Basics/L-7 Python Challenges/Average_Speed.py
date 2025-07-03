spda = float(input("Enter the speed of the first cyclist (in m/s) : "))
spdb = float(input("Enter the speed of the second cyclist (in m/s) : "))
spdc = float(input("Enter the speed of the third cyclist (in m/s) : "))
avg = (spda+spdb+spdc)/3
print("The average speed is ",avg)
if spda <= avg :
    print("The speed of the first cyclist (",spda," m/s) is below average (",avg," m/s )")
elif spdb <= avg :
    print("The speed of the second cyclist (",spdb," m/s) is below average (",avg," m/s )")
elif spdc <= avg :
    print("The speed of the third cyclist (",spdc," m/s) is below average (",avg," m/s )")
else :
    print("All the cyclists are travelling are travelling at the same speed")
    