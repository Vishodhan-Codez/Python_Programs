n = {"a":1,"b":2,"c":3,"d":4}
list1 = []
list2 = []
for i in n.values() :
    list1.append(i)
for j in n.keys():
    list2.append(j)
for k in range(len(list1)) :
#    n[list1[k]]= list2[k]
    n.update({list1[k]:list2[k]})
print(n)
