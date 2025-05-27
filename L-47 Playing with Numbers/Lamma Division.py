big = int(input("Enter the bigger number: "))
big1 = big
smal = int(input("Enter the smaller number: "))
smal1 = smal
while(smal) : # smal != 0
    store = smal
    smal = big%smal
    big = store
print("The HCF of {} and {} is {}".format(big1,smal1,store))