class Solution(object):
    def quickSort(self, arr):
        if len(arr) < 2:
            return arr
        
        pivot = arr[0]
        higher_arr = []
        lower_arr = []
        pivot_arr = [pivot]

        for num in arr[1:]:
            if num > pivot:
                higher_arr.append(num)
            elif num < pivot:
                lower_arr.append(num)
            else:
                pivot_arr.append(num)

        return self.quickSort(lower_arr) + pivot_arr + self.quickSort(higher_arr)
        # reverse order
        # return self.quickSort(higher_arr) + pivot_arr + self.quickSort(lower_arr)
        
    def quickSortNew(self,arr):
        if len(arr) < 2:
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i<=pivot]
            greater = [i for i in arr[1:] if i>pivot]
            
            return self.quickSortNew(less) + [pivot] + self.quickSortNew(greater)


    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        sorted_seats = self.quickSort(seats)
        sorted_students = self.quickSort(students)

        total_moves = 0 
        for i in range(len(sorted_seats)):
            min_moves = sorted_seats[i]-sorted_students[i]
            total_moves += abs(min_moves)

        return total_moves
    
print(Solution().minMovesToSeat([2,2,6,6],[1,3,2,6]))

print(Solution().quickSort([2,2,6,6,4,3,9,1]))