#### Binary Search - Target #### 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        LP, RP = 0, len(nums) - 1

        while LP <= RP:
            MP = (LP + RP) // 2

            if target > nums[MP]:
                LP = MP+1

            elif target < nums[MP]: 
                RP = MP-1
            
            else:
                return MP

        return -1
    
    
#### Binary Search - Range ####

# Binary search on some range of values
def binarySearch(low, high):

    while low <= high:
        mid = (low + high) // 2

        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid
    return -1


# Return 1 if n is too big, -1 if too small, 0 if correct
def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0

