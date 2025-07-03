a = 35
b = 19

"""BINARY CONVERSION """
# For a,
# 32 16 8 4 2 1
#  1  0 0 0 1 1
# 35 = 100011

# For b,
# 16 8 4 2 1
#  1 0 0 1 1
# 19 = 10011

""" AND OPERATOR (&) for a=35 and b = 19"""
# 1 0 0 0 1 1
# 0 1 0 0 1 1
# -------------
# 0 0 0 0 1 1 => 3
print(a&b)

""" OR OPERATOR (|) for a=35 and b = 19"""
# 1 0 0 0 1 1
# 0 1 0 0 1 1
# -------------
# 1 1 0 0 1 1 => 51
print(a|b)

""" XOR OPERATOR (^) for a=35 and b = 19"""
# 1 0 0 0 1 1
# 0 1 0 0 1 1
# -------------
# 1 1 0 0 0 0 => 48
print(a^b)

""" LEFT SHIFT OPERATOR (<<) for a=35"""
#   1 0 0 0 1 1
# -------------
# 1 0 0 0 1 1 0 => 70
print(a<<1)

""" RIGHT SHIFT OPERATOR (>>) for a=35"""
# 1 0 0 0 1 1
# -------------
#   1 0 0 0 1  => 17
print(a>>1)

""" LEFT SHIFT OPERATOR (<<) for b=19"""
#   1 0 0 1 1
# -------------
# 1 0 0 1 1 0   => 38
print(b<<1)

""" RIGHT SHIFT OPERATOR (<<) for b=19"""
#   1 0 0 1 1 
# -------------
#     1 0 0 1  => 9
print(b>>1)