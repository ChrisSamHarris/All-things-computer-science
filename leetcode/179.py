# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.

# Example 1:
# Input: nums = [10,2]
# Output: "210"

# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        greedy = solution | largest digits in the most significant place 
        """
        
        def compare(n1, n2):
            """
            Compare the string of numbers to decipher which is larger - return the larger significant digit 
            """
            if n1 + n2 > n2 + n1:
                return -1
            else: 
                return 1
        
        for i, num in enumerate(nums):
            nums[i] = str(num)
            
        nums = sorted(nums, key=cmp_to_key(compare))
        
        # This will resolve any issues where the list is all 0s
        return str(int("".join(nums)))
    
# Time complexity: O(nlogn)
print(Solution().largestNumber([3,30,34,5,9]))