# Search in a rotated array - Slightly modified binary search function 

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

class Solution(object):
    def search(self, nums, target):
        """
        Altered binary search:
        1) Determine which part of the array is sorted
        2) Check if the target lies in the sorted part of the array
        """
        # quicksort = n log n time complexity = Slower than O(log n)
        # binary search = O(log n)

        if len(nums) < 2:
            return 0 if nums[0] == target else -1

        LP, RP = 0, len(nums)-1

        while LP <= RP:
            mid = (LP + RP) // 2 

            if target == nums[mid]:
                return mid

            # determine which part is sorted: 
            # left part is sorted 
            if nums[LP] <= nums[mid]:
                # target lies in the left part of the array
                if nums[LP] <= target < nums[mid]:
                    RP = mid - 1
                else:
                    LP = mid + 1 
            else:
                if nums[mid] < target <= nums[RP]:
                    LP = mid + 1 
                else: 
                    RP = mid -1 

        return -1 
    
print(Solution().search([4,5,6,7,0,1,2], 3))