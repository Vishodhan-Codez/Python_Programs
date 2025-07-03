# 1**2 + 2**3
# i+= 1 , j+= 1 
n=int(input("enter the no.of terms :"))
sum,j = 0,2
for i in range(1,n+1,1) :
    sum += (i**j)
    j+= 1
print(sum)