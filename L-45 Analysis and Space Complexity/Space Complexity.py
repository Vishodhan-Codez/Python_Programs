def summ(n) :
    return n*(n+1)/2
a=summ(5)
# Here , the Space Complexity and Auxilary Space is as follows :
# SC : θ(1)
# AS : θ(1)

def array1(n) :
    sum = 0
    for i in n :
        sum += i
    return sum
list1 = [1,2,3,4,5]
b=array1(list1)
# Here , the Space Complexity and Auxilary Space is as follows :
# SC : θ(n) "5"
# AS : θ(1)

"""def sum1(n) :
    if (n<= 0):
        return 
    return n+ (sum1((n-1)))
c=sum1(6)
"""
# Here , the Space Complexity and Auxilary Space is as follows :
# SC : θ(n) "6"
# AS : θ(n) "6"

print(f"{a}\n{b}\n")
