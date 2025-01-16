low = int(input("Enter the lowest number of the range : "))
high = int(input("Enter the highest number of the range : "))
step_size = int(input("Enter how many numbers to skip : "))
for i in range(high,low,step_size) :
    print(i)
