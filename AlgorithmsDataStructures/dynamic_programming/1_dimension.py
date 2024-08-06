### Fibonacci Number 

def bruteForce(n):
    """
    Fibonacci number brute forece method. 
    Lots of repeated calculations.
    O(2^n)
    """
    if n <= 1:
        return n
    return bruteForce(n - 1) + bruteForce(n - 2)



def memoization(n, cache):
    """
    memoization method for Fibonacci number. Utilising cache to store the results of the calculations, 
    as such we don't have to recalculate the same values.
    O(n)
    """
    # Base Case
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    # Recursive Case
    cache[n] = memoization(n - 1) + memoization(n - 2)
    return cache[n]


def dp(n):
    """
    Bottom up dynamic programming method for Fibonacci number.
    O(n)
    """
    if n < 2:
        return n
    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]



### Example - Leetcode 70 

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


class Solution(object):
    def helper(self, n, cache):
        """
        memoization - top down approach with the base cases set to steps
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
            
        if n in cache:
            return cache[n]

        cache[n] = self.helper(n-1, cache) + self.helper(n-2, cache)
        return cache[n]

    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        cache = {}
        distinct = self.helper(n, cache)

        return distinct 