n = int(input("Enter a string : "))
def powersetstring(s):
    n = len(s)
    ps = []
    for i in range(1, 1 << n):
        subset = ""
        for j in range(n):
            if i & (1 << j):  
                subset += s[j]
        ps.append(subset)
    return ps

n = input("Enter a string: ")
res = powersetstring(n)
print("\nAll combinations using bitwise power set:")
for substr in res:
    print(substr)
