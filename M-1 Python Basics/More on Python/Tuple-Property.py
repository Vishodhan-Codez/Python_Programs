# Tuple Property
# (0,5,1,7,1,4,5,8,3,1,7,1,2,7)
# (i) Find no. of 7's
# (ii) Find index of first seven
# (iii) Add one more value
t = (0,5,1,7,1,4,5,8,3,1,7,1,2,7)
m = list(t)
print(t,type(t))
nos = 0
for i in m :
    if i == int(7) :
        nos += 1
        if nos == 1 :
            print("The index of the first 7 is ",m.index(i))
m.append(int(input("Enter a number to append : ")))
m = tuple(m)
print("There are",nos,"number of 7's in",m)
    
    