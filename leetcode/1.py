#### TWOSUM ####

# Example 1:
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
# Example 2:
    # Input: nums = [3,2,4], target = 6
    # Output: [1,2]
    
# Example 3:
    # Input: nums = [3,3], target = 6
    # Output: [0,1]

def twoSumA(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lp = 0 
    while True:
        for rp in range(1, len(nums)):
            if lp == rp:
                rp += 1
            if nums[lp] + nums[rp] == target:
                return [lp, rp]
            if rp == len(nums) - 1:
                lp += 1
        
print(twoSumA([3,1,2, 3, 4], 3))





def twoSumB(nums, target):
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        num_to_index[num] = i
        
print(twoSumB([2,7,11,15], 9))
    
    


        
