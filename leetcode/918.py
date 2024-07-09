# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

# Example 1:
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def Kadanes_algo(nums):
            # initialise a maxSum & curSum
            maxSum = nums[0]
            curSum = 0 

            for n in nums:
                curSum = max(curSum, 0) + n 
                maxSum = max(maxSum, curSum)
            return maxSum

        max_sum = Kadanes_algo(nums)

        total_sum = sum(nums)
        inverted_nums = [-n for n in nums]
        wrap_sum = total_sum + Kadanes_algo(inverted_nums)

        # If all numbers are negative, return the maximum (which will be the least negative)
        if wrap_sum > 0:
            return max(max_sum, wrap_sum)
        else:
            return max_sum

nums = [1,-2,3,-2]
print(Solution().maxSubarraySumCircular(nums))