#### Kadanes Algorithm
##### Find a non-empty subarray with the largest sum

def bruteForce(nums):
    """
    2 pointers. Working solution time complexity is N**2.
    """
    maxSum = nums[0]

    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum


def kadanes(nums):
    """
    Kadanes Algorithm - the maximum sum of a contiguous subarray in an array with a runtime of O(n).
    """
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        # curSum = max(curSum, 0)
        # curSum += n
        # if our current sum is less than 0, we reset it to 0.
        curSum = max(curSum, 0) + n
        maxSum = max(maxSum, curSum)
    return maxSum

print(kadanes([4,-1,2,-7,3,4]))

##### What is we want to return the indexes of the max subarray? - Sliding Window 
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R 

    return [maxL, maxR]

print(slidingWindow([4,-1,2,-7,3,4]))