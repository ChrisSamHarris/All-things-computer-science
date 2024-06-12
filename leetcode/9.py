# Given an integer x, return true if x is a 
# palindrome, and false otherwise.
 
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
# Constraints:
# -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    # Converting to a string: 
    str_num = str(x)
    return str_num[::-1] == str_num

def is_palindrome(x: int) -> bool:
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Numbers ending in 0 are not palindromes unless the number is 0
    if x % 10 == 0 and x != 0:
        return False
    
    # Reverse half of the number and compare
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
    return x == reversed_half or x == reversed_half // 10

# Test cases
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121)) # Output: False
print(is_palindrome(10))   # Output: False
