# To check if a number is Palindrome
a = int(input("Enter the no.of elements in the list : "))
n = []
for i in range(1,a+1):
    n.append(int(input(f"Enter element {i} : ")))

n1 = n
n.reverse()
if n1 == n :
    print("The list is a palindrome")
else :
    print("The list is not palindrome")
