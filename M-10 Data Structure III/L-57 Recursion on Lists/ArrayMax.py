def ArrayMax(a) :
    if len(a) == 1 :
        return a[0]
    return max(a[0],ArrayMax(a[1:]))
a = [1,2,567,34,89,180,1000]
print(f"The largest value in the list -\n{a}\nis {ArrayMax(a)}")