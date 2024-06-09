# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def dfs(i,j):
            """As we've already counted the island, turn the island to water"""
            # ensure row index is in the grid, ensure column is within row, ensure you're on land
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                # dfs on right
                dfs(i, j+1)
                # dfs on bottom
                dfs(i+1, j)
                # dfs on left
                dfs(i, j-1)
                # dfs above
                dfs(i-1, j)

        num_islands = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i,j)
        
        return num_islands
    

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

islands = Solution().numIslands(grid)
print(islands)