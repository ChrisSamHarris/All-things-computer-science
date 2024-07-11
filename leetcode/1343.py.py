# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

# Example 1:
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        window_sum = 0  # Sum of current window
        count = 0  # Count of valid subarrays
        L = 0

        for R in range(len(arr)):
            window_sum += arr[R]
            
            # Check if window size is k | + 1 due to index starting at 0 
            if (R - L) + 1 == k:
                # Check if average meets or exceeds threshold
                if (window_sum / k) >= threshold:
                    count += 1
                
                # Remove leftmost element from sum and move left pointer
                window_sum -= arr[L]
                L += 1
            
        return count
    
print(Solution().numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))