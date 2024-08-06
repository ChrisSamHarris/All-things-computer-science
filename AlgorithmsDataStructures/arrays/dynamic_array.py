class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return nums + nums   

        return nums + [i for i in nums[:]]
    

    
    