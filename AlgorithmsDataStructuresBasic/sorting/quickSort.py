class Solution(object):
    def sortArray(self, nums):
        """
        QuickSort with a median index 
        Divide and conquer algorithm 
        
        The target of partitions is to place the pivot (any element can be chosen to be a pivot) at its correct position in the sorted array and put 
        all smaller elements to the left of the pivot, and all greater elements to the right of the pivot.
        Partition is done recursively on each side of the pivot after the pivot is placed in its correct position and this finally sorts the array.
        """
        if len(nums) <  2:
            return nums

        else:
            mid_index = len(nums) // 2
            pivot = nums[mid_index]

        less = [i for i in (nums[:mid_index] + nums[mid_index + 1:]) if i <= pivot]
        greater = [i for i in (nums[:mid_index] + nums[mid_index + 1:]) if i > pivot]

        return self.sortArray(less) + [pivot] + self.sortArray(greater)
    
    