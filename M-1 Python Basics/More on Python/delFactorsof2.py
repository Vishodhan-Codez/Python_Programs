n = {"A":4,"B":3,"C":7,"D":0,"E":1}
nos = []
for i,j in (n.items()):
    if j%2 == 0 :
        nos.append(i)
for _ in nos :
    del n[_]
print("The edited dictionary is ",n)

n2 = {"A":4,"B":3,"C":7,"D":0,"E":1}
nos2 = {}
for g in n2 :
    if n2[g]%2 == 0 :
        del n2[g]
print("The edited dictionary is ",n2)
