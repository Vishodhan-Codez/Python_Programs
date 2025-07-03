#Write a python program to return the numbers in a tuple b(10,20,30,40,50,60,70) whoose sum is equal to the number inputed by the user. Also print thier index numbers :
class NumberSearch :
    def twosum(self,nums,target) :
        lookup = {}
        for i,num in enumerate(nums) : #enumarate take index and value
            if target - num in lookup: # is found
                return lookup[target-num],i
            lookup[num] = i
obj1 = NumberSearch()
n = int(input("Enter a target to the find any sum of two numbers and return their index : \n"))
tupla = (10,20,30,40,50,60,70)
print(obj1.twosum(tupla,n))
