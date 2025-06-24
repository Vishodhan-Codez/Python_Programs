def powerset(set,setsize) :
    setpower = 2**setsize
    outer = 0
    inner = 0
    print(f"\nThe diffrent set combinations for \n{set} are :",end="")
    for outer in range(setpower) :
        for inner in range(setsize) :
            if (outer&(1<<inner)) > 0 :
                print(set[inner],end="")
        print(" ")
set = []
s = int(input("Enter the length of the list : "))
for i in range(s) :
    set.append(int(input("Enter the next element : ")))
powerset(set,s)