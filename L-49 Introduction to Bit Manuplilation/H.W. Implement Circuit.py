a = 1
b = 1
c = 0

g1 = a | b
g2 = a & c
g3 = b & c
g4 = g2 | g3
q = g1 & g4

print(q)
