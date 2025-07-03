a = input("Enter a group of words : ")
l=a.split(' ')
l.reverse()
sum = ''
for i in l :
    sum += (i+' ')
print(sum)
