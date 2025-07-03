def myfunction1(n):
    if n <= 0:
        return
    for i in range(0, n + 1):
        print("Codingal")
    myfunction1(n // 2)
    myfunction1(n // 3)

# Time Complexity :
# T = T(n/2) + T(n/3) + θ(n) [if n > 0]
# T = T(1) [if n <= 0]

# Time Complexity Map
#                     T(n)
#                 /         \
#           T(n/2)         T(n/3)
#           /    \         /     \
#     T(n/4) T(n/6)   T(n/6)  T(n/9) 
#     (n/2)/2 (n/2)/3 (n/3)/2 (n/3)/3 - took help from google as did not understand clearly
#         ...           ...           ...


# Time Complexity: O(n)


def myfunction2(n):
    if n <= 1:
        return
    print("Codingal")
    myfunction2(n - 1)

# Space Complexity: θ(1)
# Auxillary Space: θ(n)
