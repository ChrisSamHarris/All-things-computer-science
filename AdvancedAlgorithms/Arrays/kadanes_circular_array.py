##### Find a non-empty subarray with the largest sum in a circular array
def findMaxSumCircular(nums):
    """
    If an array is circular we need to consider:1
    1) The maximum sum subarray in the linear array (Kadanes)
    2) The total sum of the array minus the minimum sum subarray in the linear array
    
    1. Use Kadane's algorithm to find the maximum sum subarray treating the array as linear. This covers the non-wrapping case.
    2. Calculate the total sum of the array and find the minimum sum subarray (by inverting the array and using Kadane's algorithm again). Subtracting this minimum sum from the total sum gives us the maximum sum of a wrapping subarray.
    3. Compare these two results (wrapping and non-wrapping) and return the larger one.
    """
    def kadanes(nums):
        """
        Kadanes Algorithm - the maximum sum of a contiguous subarray in an array with a runtime of O(n)- linear time. 
        If the curSum isn't greater than 0, we reset it to 0.
        """
        
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0) + n
            maxSum = max(maxSum, curSum)
        return maxSum
    
    # 1. Max subarray sum in a linear array
    max_sum = kadanes(nums)
    
    # 2. Max subarray sum in a circular array
    total_sum = sum(nums)
    minSumSubarray = [-n for n in nums]
    min_sum = kadanes(minSumSubarray)
    
    # We calculate the maximum sum possible in a circular configuration.
    # Mathmatically: max_circular_sum = total_sum - min_sum
    circular_max = total_sum + min_sum
    
    # handle edge cases where all numbers are negative
    return max(max_sum, circular_max) if circular_max > 0 else max_sum

print(findMaxSumCircular([-3,-2,-3]))
print(findMaxSumCircular([5,-3,5]))

# In the context of finding the maximum subarray sum in a circular array, identifying the minimum sum subarray
# allows us to effectively "remove" it from the total sum, which is equivalent to wrapping around the array ends. 

# By inverting the signs, the subarray that had the smallest (most negative) sum in the original array will have the largest (most positive) sum 
# in the inverted array. This clever trick lets us solve the minimum sum problem using the same efficient approach we use for the maximum sum problem.