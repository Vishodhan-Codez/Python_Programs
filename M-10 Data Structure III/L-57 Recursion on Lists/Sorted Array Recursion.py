def sorted1(a) :
    if len(a) == 1 or len(a) == 0 :
        print("The list is already sorted")
        return True
    return a[1] >= a[0] and sorted1(a[1:])
a = [1,2,3,4,5,6,7,51]
if sorted1(a) == False :
    print("The list is not sorted")