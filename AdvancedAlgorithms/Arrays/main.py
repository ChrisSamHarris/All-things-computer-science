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


#### Sliding Window Fixed Size 
##### Q: Given an array, return true if there are two elements within a window of size k that are equal.

## Loop Solution - Brute Force 
def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        # min(len(nums), L + k) is used to avoid index out of range
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


## Hashset solution
def closeDuplicates(nums, k):
    window = set() # Cur window of size <= k
    L = 0

    for R in range(len(nums)):
        if (R - L) + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False

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
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length

#### Two Pointers

#### Prefix Sums
