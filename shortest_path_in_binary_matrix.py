from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        self.__bfs(grid, visited, 0, 0)
        
    def __bfs(self, grid: List[List[int]], visited: List[List[bool]], i: int, j: int):
        m, n = len(grid), len(grid[0])
        if i == m - 1 and j == n - 1:
            return 1
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1 or visited[i][j]:
            return -1
        visited[i][j] = True
        res = -1
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            res = max(res, self.__bfs(grid, visited, x, y))
        return res + 1
        