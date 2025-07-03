try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age cannot be negative.")
    else:
        if age %2== 0:
            print(f"The age {age} is even.")
        else:
            print(f"The age {age} is odd.")
except ValueError:
    print(f"Invalid input. Please enter a valid number for age.\n{ValueError}")
