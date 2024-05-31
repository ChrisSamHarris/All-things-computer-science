# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.

class Solution(object):
    def quickSort(self, arr: list[int], s: int, e: int) -> list[int]:
        """
        this wont submit due to time limit complexity within Leetcode
        """
        if e - s + 1 <= 1:
            return arr

        pivot = arr[e]
        left = s # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(s, e):
            if arr[i] < pivot:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        # Move pivot in-between left & right sides
        arr[e] = arr[left]
        arr[left] = pivot
        
        # Quick sort left side
        self.quickSort(arr, s, left - 1)

        # Quick sort right side
        self.quickSort(arr, left + 1, e)

        return arr
   
array = [5,2,3,1,99,27,33,27,28,90,45,65,999,12,15,26,36,48,55,61,70,80,85,1,1,5,7,76,23]
sol = Solution().quickSort(array, 0, len(array)-1)
print(sol)


                
        
                