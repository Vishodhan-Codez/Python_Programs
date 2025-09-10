def max1(a,l):
    count = 0
    max1s = 0
    for i in a :
        if i == 0 :
            count = 0
        else : 
            count += 1 
            max1s = max(max1s,count)
    return max1s
arr = [1,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1]     
print("The maximum count of 1's in\n",arr,"\nis",max1(arr,len(arr))) 