def subArraySum(arr, n, sum_):
    for i in range(n) :
        cs = arr[i]
        j = i + 1 
        while j <= n:
            if cs == sum_:
                print ("Sum found between")
                print("indexes % d and %d"%(i, j-1))
                return 1
            if cs > sum or j == n: 
                break
            cs = cs + arr[j]
            j += 1
    print ("No subarray found")
    return 0
arr = [3,6,2,2,56,1,0,9]
n = len(arr)
sum = 10
subArraySum(arr, n, sum)