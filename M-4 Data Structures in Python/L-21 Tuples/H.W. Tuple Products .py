tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)
def calculate_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product
pro1 = calculate_product(tup1)
pro2 = calculate_product(tup2)
print(f"The product of tup1 is: {pro1}")
print(f"The product of tup2 is: {pro2}")
