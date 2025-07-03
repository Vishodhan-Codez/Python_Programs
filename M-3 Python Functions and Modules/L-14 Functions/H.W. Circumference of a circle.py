def calc(r):
    if r < 0:
        return "Radius cannot be negative. Please enter a positive value."
    else:
        circumference = 2 * 3.14159 * r
        return "The circumference of the circle is: ",circumference
a= float(input("Enter the radius of the circle: "))
print(calc(a))
