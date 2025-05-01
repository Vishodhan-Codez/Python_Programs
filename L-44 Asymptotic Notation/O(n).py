def O(n) :
    iterations = 0
    for i in range(n):
        iterations += 1 
    print(f"When 'n' is {n}\nNo.of Iterations : {iterations}")

O(10)
O(30)
O(42)

# We see that as the value of n increases the no.of iterations proportionally increase with a constant of 1
