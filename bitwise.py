#bitwise operators
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
a << 2            # 240 = 1111 0000 same as 60 * 2^2
a >> 2            # 15  = 0000 1111 same as 60 / 2^2
a & b             # 12 = 0000 1100 (AND)
a | b             # 61 = 0011 1101 (OR)
a ^ b             # 49 = 0011 0001 (XOR)
~a               # -61 = 1100 0011 (NOT)
# Note: Python does not have unsigned integers, so the result of NOT is -x-1