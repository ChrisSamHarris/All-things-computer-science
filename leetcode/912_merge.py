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
    def merge(self, arr, s, m, e):
    # Copy the sorted left & right halfs to temp arrays
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # One of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, nums, s,e):   
        if e - s + 1 <= 1:
            return nums

        m = (s + e) // 2

        self.mergeSort(nums, s=s, e=m)

        self.mergeSort(nums, s=m + 1, e=e)

        self.merge(nums, s=s, m=m, e=e)
        
        return nums

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        NOTE: This solution will work at a much greater speed than insertion 
        """
        ##### Insert Sort - This wont work as its too slow 
        # for i in range(1, len(nums)):
        #     j = i-1
        #     while j >= 0 and nums[j+1] < nums[j]:
        #         temp = nums[j+1]
        #         nums[j+1] = nums[j]
        #         nums[j] = temp
        #         j -= 1

        # return nums

        s = 0
        e = len(nums) - 1

        return self.mergeSort(nums=nums, s=s, e=e)

sol = Solution().sortArray([5,2,3,1,99,27,33,27,28,90,45,65,999,12,15,26,36,48,55,61,70,80,85,1,1,5,7,76,23])
print(sol)


                
        
                