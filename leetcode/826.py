class Solution(object):
    def quickSort(self, arr):
        """
        Recursively call quickSort on the left array and right array 
        """
        # base case
        if len(arr) < 2: 
            return arr 

        # Recursive case 
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]

        return self.quickSort(left) + [pivot] + self.quickSort(right)
        
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        sorted_workers = self.quickSort(worker)
        
        # Create a list of (difficulty, profit) tuples and sort it by difficulty
        jobs = sorted(zip(difficulty, profit), key=lambda x: x[0])
        
        max_profit = 0
        temp_profit = 0 
        job_index = 0 
        
        for worker_skill in sorted_workers:
            # Assign the best possible job to the worker
            while job_index < len(jobs) and worker_skill >= jobs[job_index][0]:
                temp_profit = max(temp_profit, jobs[job_index][1])
                job_index += 1
            max_profit += temp_profit

        return max_profit
        
  
    
print(Solution().quickSort([3,6,8,10,1,2,1]))

print(Solution().maxProfitAssignment(difficulty=[2,4,6,8,10], profit=[10,20,30,40,50], worker=[4,5,6,7]))
print(Solution().maxProfitAssignment(difficulty=[85,47,57], profit=[24,66,99], worker=[40,25,25]))