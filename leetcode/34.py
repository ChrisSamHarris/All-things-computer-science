# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        LP, RP = 0, len(nums)-1
        start_end = []

        if len(nums) < 2: 
            if len(nums) == 0:
                return [-1,-1]
            elif target == nums[0]:
                return [0,0]

        while LP <= RP: 
            mid = (LP + RP) // 2 

            if nums[mid] == target:
                
                original_mid = mid-1
                while mid <= len(nums) -1 and nums[mid] == target:
                    if nums[mid] == target:
                        start_end.append(mid)
                        mid += 1
                        
                while original_mid >= 0 and nums[original_mid] == target:
                    if nums[original_mid] == target:
                        start_end.insert(0,original_mid)
                        original_mid -=1
                
                if len(start_end) == 1:
                    start_end.append(start_end[0])
                elif len(start_end) > 2:
                    start_end = [start_end[0], start_end[-1]]
                    
                return start_end
            
            elif nums[mid] > target:
                RP = mid -1 

            else:
                LP = mid+1 
        
        start_end = [-1,-1]
        return start_end

print(Solution().searchRange([2,2], 2))
print(Solution().searchRange([5,7,7,8,8,10], 8))



class SolutionNeet(object):
    def binSearch(self, nums, target, leftBias):
        """
        BS function. LeftBias = [True/False]
        """
        LP, RP = 0, len(nums)-1
        i =-1
        
        while LP <= RP: 
            mid = (LP + RP) // 2 
            
            if nums[mid] == target:
                i = mid
                #  Utilise the bias condition 
                if leftBias:
                    RP = mid -1
                else:
                    LP = mid +1
                    
            elif nums[mid] > target:
                RP = mid -1 
                
            else:
                LP = mid+1 
                
        return i
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        
        return [left,right]

print(SolutionNeet().searchRange([2,2], 2))
print(SolutionNeet().searchRange([5,7,7,8,8,10], 8))