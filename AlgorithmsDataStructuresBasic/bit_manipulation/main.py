# AND
n = 1 & 1

# OR
n = 1 | 0

# XOR
n = 0 ^ 1

# NOT (negation)
n = ~n

# Bit shifting
n = 1
n = n << 1
n = n >> 1


# Counting Bits
# Let us say that we are asked to count the number of 1 bits that are in the binary representation of the integer 23.
def countBits(n):
    """
    Quotient and remainder method - count the number of 1 bits in the binary representation of a number.
    """
    count = 0
    while n > 0:
        # comparison is done with bits i.e. 10111 & 00001 -> 010111 & 00001 -> 001011 & 00001 -> 000101 & 00001 -> 000010 & 00001 -> 000001 & 00001
        # AND operations isolates the right most bit of n because of how the binary operation works 
        if (n & 1) == 1:
            count += 1
            
        # iterate and shorted the number by shifting to the right
        n = n >> 1 # same as n // 2
    return count

print(countBits(23))

# 23 = 10111

# // First bit was a 1, increment count and shift to the right.
# 10111 & 00001 -> 00001

# // First bit was a 1, increment count and shift to the right.
# 01011 & 00001 -> 00001

# // We again get a 1, so increment count and shift to the right.
# 00101 & 00001 -> 00001

# // We get a 0, so we only shift to the right, leaving the count untouched.
# 00010 & 00001 -> 00000

# // We get a 1, so we shift to the right and increment the count.
# 00001 & 00001 -> 00001


#   Step   |  Dividend  |  Quotient  |  Remainder  |  Notes
# ---------|------------|------------|-------------|-----------------------
#    1     |     23     |     11     |      1      | Least significant bit
#    2     |     11     |      5     |      1      |
#    3     |      5     |      2     |      1      |
#    4     |      2     |      1     |      0      |
#    5     |      1     |      0     |      1      | Most significant bit
