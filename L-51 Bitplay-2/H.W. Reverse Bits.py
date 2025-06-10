def rev_bits(n):
    rev = 0
    for _ in range(n.bit_length()):
        rev = (rev << 1) | (n & 1)
        n >>= 1
    return rev

n = int(input("Enter number: "))
r = rev_bits(n)
print(f"Reversed Number: {r}")