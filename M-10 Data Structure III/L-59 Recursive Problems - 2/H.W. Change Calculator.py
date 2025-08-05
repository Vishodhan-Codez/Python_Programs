def ways(n, i, currency):
    if n == 0:
        return 1
    if n < 0 or i == len(currency):
        return 0
    use = ways(n - currency[i], i, currency)   # Use the current coin
    skip = ways(n, i + 1, currency)            # Skip the current coin
    return use + skip
currency = [500, 100, 10, 5, 1]
n = int(input("Enter the amount of rupees you have -\n₹"))
print(ways(n, 0, currency))
