def sim(m,n) :
    for i in m :
        for j in n :
            if i == j :
                print(i,end=" , ")
    return
m = eval(input("Enter a list in '[]' - \n"))
n = eval(input("Enter another list in '[]' - \n"))
print("The common elements are - ")
sim(m,n)

map(m,n) 