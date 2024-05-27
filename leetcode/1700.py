from collections import Counter

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = len(students)
        # cnt = Counter(students)
        
        map_food = {}
        for s in students:
            if s not in map_food:
                map_food[s] = 0
            map_food[s] +=1
        
        for s in sandwiches:
            try: 
                if map_food[s] > 0:
                    map_food[s] -= 1
                    count -= 1
                else: 
                    return count
            except:
                return count

        return count
            
            
        
sol = Solution().countStudents([1,1,0,0], [0,1,0,1])
print(sol)

sol2 = Solution().countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])
print(sol2)     

sol3 = Solution().countStudents([1,1], [0,1])
print(sol3)  



class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = 0  # Counter to track the number of unsuccessful attempts to eat

        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0  # Reset counter when a sandwich is taken
            else:
                students.append(students.pop(0))
                count += 1
            
            if count == len(students):  # If all students have been checked and no one ate
                return len(students)

        return 0  # All students have taken their sandwiches

# Example usage:
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
solution = Solution()
print(solution.countStudents(students, sandwiches))  # Output: 0
