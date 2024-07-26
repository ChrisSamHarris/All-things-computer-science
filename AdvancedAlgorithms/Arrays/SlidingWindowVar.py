#### Sliding Window Variable Size
##### Q: Find the length of the longest subarray, with the same value in each position.
def longestSubarray(nums):
    length = 0
    L = 0
    
    for R in range(len(nums)):
        # is the value of LEFT and RIGHT the same 
        if nums[L] != nums[R]:
            L = R 
        length = max(length, R - L + 1)
    return length

##### Q: Find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive.
def shortestSubarray(nums, target):
    L, total = 0, 0
    length = float("inf")
    
    for R in range(len(nums)):
        total += nums[R]
        
        # Embed a while loop to progress L in order to work to the smallest subarray
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
            
    return 0 if length == float("inf") else length