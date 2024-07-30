##### Q: Given an array of values, design a data structure that can query the sum of a subarray of the values

class PrefixSum:
    def __init__(self, nums):
        """
		Build the prefix array - O(n)
		"""
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
    
    def rangeSum(self, left, right): 
        """
        Using the prefix array, calculate the difference - O(1)
        """
        preRight = self.prefix[right]
		# stops us going out of bounds 
        preLeft = self.prefix[left - 1] if left > 0 else 0
        
        return (preRight - preLeft)
 