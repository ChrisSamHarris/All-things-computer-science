class SolutionCD(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Given an integer array nums, return true if any value appears at 
        least twice in the array, and return false if every element is distinct.
        """
        # seen_nums = []
        # for num in nums:
        #     if num in seen_nums:
        #         return True
        #     else:
        #         seen_nums.append(num)
        # return False
        return len(nums) != len(set(nums))
    
    
    
class SolutionRE(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        Given an integer array nums and an integer val, remove all occurrences of val
        in nums in-place. The order of the elements may be changed. Then return the number 
        of elements in nums which are not equal to val.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # partition 
                nums[k] = nums[i]
                k += 1 
            # if we index at val, we want to skip 
        return k 

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        concatenate a list of numbers 
        Input: nums = [1,2,1]
        Output: [1,2,1,1,2,1]
        """
        return nums + nums
    
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lp = 1 

        for rp in range(1, len(nums)):
            if nums[rp] != nums[rp-1]:
                nums[lp] = nums[rp]
                lp += 1 

        return lp
    
    
