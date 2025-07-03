amount = int(input("Enter the total amount (in $) : "))
n2000 = (amount//2000)
amount = amount%2000
n500 = (amount//500)
amount = amount%500
n100 = amount//100
amount = amount%100
n50 = amount//50
amount = amount%50
n10 = amount//10
amount = amount%10
print("You need ",n2000," Rs.2000 notes and ",n500," Rs.500 notes and ",n100," Rs.100 notes and ",n50," Rs.50 notes and ",n10," Rs.10 notes and ",amount," Rs.1 coins.")