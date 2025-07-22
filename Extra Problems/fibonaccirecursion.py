def fibbonacci(l):
    if l <= 1 :
        return l
    return fibbonacci(l-1)+fibbonacci(l-2)
l = int(input("Enter the length of the series : "))
for i in range(l) :
    print(fibbonacci(i),end=" | ")
    