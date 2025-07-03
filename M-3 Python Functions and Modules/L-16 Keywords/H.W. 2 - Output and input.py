# input - 40,10,20,80,50,60
# output - 80,40
nums = [40, 10, 20, 80, 50, 60]
res = []
for n in nums:
    if n % 10 != 0:
        continue
    res.append(n)
    if len(res) == 2:
        break
print(f"{res[0]},{res[1]}")