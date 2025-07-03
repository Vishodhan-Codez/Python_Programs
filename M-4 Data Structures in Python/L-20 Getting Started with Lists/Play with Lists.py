import random
lista,sum,h,l =[],0,0,10000
for i in range(0,100) :
    a = random.randint(1,10000)
    lista.append(a)
print(lista)
for i in lista :
    sum += i
    if i > h :
        h = i
    if i < l :
        l = i
print("Sum of all numbers : ",sum)
print("The average is :",sum/len(lista))
print("The highest number is ",h,"\nThe lowest number is ",l)

               

