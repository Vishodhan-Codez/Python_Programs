choice = input("Enter '1' to convert Decimal to Binary or '2' to convert Binary to Decimal: ")
if choice == '1':
    decimal = int(input("Enter a decimal number: "))
    binary = ""
    current = decimal
    while current > 0:
        remainder = current%2
        binary = str(remainder) + binary
        current //= 2
    print("Binary representation:", binary)
elif choice == '2':
    binary = input("Enter a binary number: ")
    decimal = 0
    power = 0

    for digit in reversed(binary):
        if digit == '1':
            count = power
            result = 1
            while count > 0:
                result *= 2
                count -= 1
            decimal += result
        power += 1

    print("Decimal representation:", decimal)
else :
    print("Enter the correct digit.")
    exit()