arr = [1,4,5,7,8,9,-2,37,7,8,899,7,-987,5,6,-19,0,45,1376,48,-4,-813,74,-8,-74,435,-137,81111]
def search(element,arr,index=0):
    if arr[index] == element :
        return "Element is found"
    if index == len(arr)-1 :
        return "Element not found"
    return search(element,arr,index+1)
print(arr)
print(search(int(input("Enter a number to serach in the above list : ")),arr))