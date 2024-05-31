# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.

class Solution(object):
    def insertionSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        NOTE: This implementation is too slow on LC and is used for smaller arrays 
        """
        for i in range(1, len(nums)):
            j = i-1
            while j >= 0 and nums[j+1] < nums[j]:
                # nums[j] and nums[j+1] are out of order so swap them over
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
                j -= 1

        return nums
   
sol = Solution().insertionSortArray([5,2,3,1,99,27,33,27,28,90,45,65,999,12,15,26,36,48,55,61,70,80,85,1,1,5,7,76,23])
print(sol)


                
        
                