from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area
                
    def dfs(self, grid: List[List[int]], i, j) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return 1 + self.dfs(grid, i - 1, j) + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j - 1) + self.dfs(grid, i, j + 1)
      
if __name__ == "__main__":
    s = Solution()
    print(s.maxAreaOfIsland(
      [[0,0,1,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,1,1,0,1,0,0,0,0,0,0,0,0],
       [0,1,0,0,1,1,0,0,1,0,1,0,0],
       [0,1,0,0,1,1,0,0,1,1,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    
    print(s.maxAreaOfIsland(
      [
        [0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,1,1,0,1,1,0,0],
        [0,1,0,0,0,1,0,0],
        [0,1,0,0,0,1,0,0]
      ]))