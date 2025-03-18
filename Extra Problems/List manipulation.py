nos = [12,45,78,23,56,89,13,90,67,14]
print(f"The index of 89 is {nos.index(89)}")
nos.sort(reverse=True)
print("The numbers in descending order are ",end="")
print(nos)
print(f"The maximum is {max(nos)}",f"The minimum is {min(nos)}",f"The sum of the numbers is {sum(nos)}",f"The average of the numbers is {sum(nos)/len(nos)}",sep="\n")