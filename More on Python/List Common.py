#Find the common between two lists
l1 = [1,2,3,4,5,6,7,8,8]
l2 = [0,1,7,9,105,5,2,8,2]
# Program :
l1 = set(l1)
l2 = set(l2)
print(l1.intersection(l2))