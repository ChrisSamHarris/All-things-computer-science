# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution(object):
    def isValid(self, s):
        """
        stack of characters 
        opening brackets are pushed to the top of the stack
        closing bracket -> check top of the stack for opening, if so pop and move on 
        """

        stack = []

        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for i in s:
            if i not in bracket_map:
                stack.append(i)
            else:
                if not stack or bracket_map[i] != stack[-1]:
                    return False
                stack.pop()

        # is theres still items in the stack, theres no palindrome 
        if len(stack) != 0:
            return False 

        return True