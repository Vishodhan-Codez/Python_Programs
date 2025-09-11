def dupfinder(l1,l2,l3=[]) :
    for i in l1 :
        if i not in l2 :
            l3.append(i)
    print(l3)
def sets0(l1,l2) :
    l1 = set(l1)
    l2 = set(l2)
    print(l1.symmetric_difference(l2))
l1 = [1,2,3,4]
l2 = [4,1,2]
print(f"The non-similar elements in \n{l1},\n{l2} are")
dupfinder(l1,l2)
# sets0(l1,l2)