# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.


# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]


# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# How do we eliminate duplicate combinations ? 

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(i, curr, total):
            if total == target:
                result.append(curr[:])
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i,curr,total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        return result
        
print(Solution().combinationSum([2,5,7], 8))
print(Solution().combinationSum([2,3,6,7], 7))