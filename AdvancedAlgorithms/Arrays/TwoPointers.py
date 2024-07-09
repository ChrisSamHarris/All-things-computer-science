#### Two Pointers
#### Q. Check if an array is palindrome 
def isPalindrome(word):
    """Compare the values of the two pointers at each space"""
    L, R = 0, len(word) - 1
    while L < R:
        if word[L] != word[R]:
            return False
        L += 1
        R -= 1
    return True

#####*Q: Given a sorted input array, return the two indices of two elements which sums up to the target value. Assume there's exactly one solution.*
def targetSum(nums, target):
    """
    2 pointers. initialise at the start & end of the array and move them towards each other.
    Big O(n) time complexity.
    """
    L, R = 0, len(nums) - 1
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            return [L, R]