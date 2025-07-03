n = 5
m = 6
# & (AND Operator)
print(m&n)
# For m = 6
# 4 2 1
# 1 1 0
# For n = 5 
# 4 2 1 
# 1 0 1
# -----------
# 1 0 0 => 4 

# | (OR Operator)
print(m|n)
# For m = 6
# 1 1 0
# 1 0 1
# -----------
# 1 1 1 => 7

# ~ (NOT Operator)
print(~m) # -7
print(~n) # -6

# ^ (XOR Operator)
print(m^n)
# For m = 6
# 1 1 0
# 1 0 1
# -----------
# 0 1 1 => 3

# >> (Right Shift)
print(m>>1)
# For m = 6
# 1 1 0
# 0 1 1 => 3 

# << (Left Shift)
print(m<<1)
# For m = 6
#   1 1 0
# 1 1 0 0 => 12