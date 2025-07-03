leist = []
n = int(input("Enter the number of elements : "))
for i in range(1,n+1) :
    leist.append(int(input(f"Enter the {i}th element : ")))
luest = []
for i in leist :
    if i not in luest :
        luest.append(i)
print(f"The list with no duplicates is {luest}")

# reversing
laust = leist[::-1]
print(laust," is the reversed list")

current = 0
leist1 = leist
for i in range(len(leist)) :
    for j in range(i+1,len(leist)) :
        if leist[i] > leist[j] :
            leist[i],leist[j] = leist[j],leist[i]
print(leist," is the reordered , ascending list." )
leist = leist1