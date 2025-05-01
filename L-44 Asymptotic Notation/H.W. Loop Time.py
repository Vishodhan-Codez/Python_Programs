def myfunction(n):
    for i in range(0, n+1):
        print("First Loop")
    # First loop: runs from 0 to n+1, so total (n+1) iterations
    # Time complexity: O(n)

    j = 1
    while j <= n+1:
        print("Second Loop", j)
        j = j * 2
    # Second loop: j doubles each time until it exceeds n+1
    # Since the no.of iterations is slowly grows by doubling, it will need lesser iterations than n
    # Time complexity: No.of iterations is always lesser than n O(<n)

    for i in range(0, 100):
        print("Third Loop")
    # Third loop: runs from 0 to 99, constant 100 iterations
    # Time complexity: O(1), as it will only take constant time
