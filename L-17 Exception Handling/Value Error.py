try:
    n = int(input("Enter a number"))
    print(f"The number is {n}")
except ValueError as ex :
    print(ex)