# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Lengths of haystack and needle
        h_len, n_len = len(haystack), len(needle)
        
        # If needle is empty, return 0
        if n_len == 0:
            return 0
        
        # Slide through the haystack - limit the range to avoid out of bounds i.e. if needle is 3 but haystack is 10 there's 
        # no need to check the last 2 characters
        for i in range(h_len - n_len + 1):
            # Check if the substring matches - sliding windows
            # gives us a substring of length n_len, starting at index i 
            if haystack[i:i + n_len] == needle:
                return i
        
        # If no match is found
        return -1
    
print(Solution().strStr("sadbutsad", "sad")) # Output: 0
print(Solution().strStr("leetcode", "leeto")) # Output: -1