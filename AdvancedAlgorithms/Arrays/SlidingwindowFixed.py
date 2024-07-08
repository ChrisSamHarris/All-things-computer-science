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
    """
    Hashset can be used to check for duplicates in a window of size k.
    """
    window = set() # Cur window of size <= k
    L = 0

    for R in range(len(nums)):
        if (R - L) + 1 > k:
            window.remove(nums[L])
            L += 1
        # constant time operation
        if nums[R] in window:
            return True
        window.add(nums[R])
        
    return False