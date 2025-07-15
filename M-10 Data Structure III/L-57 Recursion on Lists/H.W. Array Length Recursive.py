def recursionlen(lst1):
    if lst1 == []:
        return 0
    return 1 + recursionlen(lst1[1:])
data = [3, 5, 7, 9, 11]
size = recursionlen(data)
print("List size:", size)
