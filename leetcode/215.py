import heapq
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?


# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[- k]
    
sol = Solution().findKthLargest([3,2,1,5,6,4], 2)
print(sol)

sol2 = Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(sol2)


#### Achieving without using .sort() 

class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l,r): 
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1 
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(1, p - 1)

            elif p < k : 
                return quickSelect(p + 1, r)

            else:
                return nums[p]
        
        return quickSelect(0, len(nums)-1)
        
    
sol = Solution2().findKthLargest([3,2,1,5,6,4], 2)
print(sol)

sol2 = Solution2().findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(sol2)

class Solution3(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

sol = Solution3().findKthLargest([3,2,1,5,6,4], 2)
print(sol)

sol2 = Solution3().findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(sol2)
