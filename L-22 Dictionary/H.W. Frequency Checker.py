d = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Dict:", d)
v = int(input("Value to check: "))
f = list(d.values()).count(v)
print(f"Frequency: {f}")
