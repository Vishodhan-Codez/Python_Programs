# num - 5/ 3 break 
n = int(input("Enter a number : "))
for i in str(n):
    if i == 3 or i == 5 :
        print(f"{i} is found in {n}")
        break
    else :
        print("5 or 3 not found .")
