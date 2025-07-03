n = int(input("Enter a number : "))
temp = n
streak = 0
mxstreak = 0
temp = bin(temp)[2:]
for i in temp :
    if i == "1" :
        streak += 1
        if streak > mxstreak :
            mxstreak = streak
    else :
        streak = 0 
if streak > mxstreak :
    mxstreak = streak
print(f"The longest streak of 1's is {mxstreak} times in {n}({temp})")