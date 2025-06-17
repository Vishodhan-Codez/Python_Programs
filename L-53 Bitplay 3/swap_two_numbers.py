def swap1(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"The numbers after swapping are {a} and {b}\n\n")
def swap2(a,b) :
    a = (a&b) + (a|b)
    b = a + ~(b) +1
    a = a + ~(b) +1 
    print(f"The numbers after swapping are {a} and {b}")
c = int(input('Enter a number : '))
d = int(input("Enter another number : "))
print(f"The numbers before swapping are {c} and {d}")
swap1(c,d)
swap2(c,d)