# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            """
            Treating array as a tree structure, iterate through all potential possiblities 
            """
            if i == n:
                res.append(sol[:])
                return 

            # explores the subset without including nums[i]
            backtrack(i+1)

            # explores the subset including nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            ## Removes nums[i] from sol to backtrack and explore other subsets 
            sol.pop()
        
        backtrack(0)
        return res
    
print(Solution().subsets([1,2,3]))
print(Solution().subsets([1,2]))