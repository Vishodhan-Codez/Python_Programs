import array as a
b = a.array('u',["a","b","c","d","e"])
print(f"The converted "+str(b))
b.append("g")
b.pop(2)
print(f"The new string is {b}")
c = b.reverse()
print(c)
print(b.count(3))