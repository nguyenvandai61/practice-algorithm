from typing import List


class Solution:
    def plant_tree(self, list: List, m: int, n: int, y: int, x: int):
        if y < 0 or x < 0 or y >= m or x >= n:
            return
        if list[y][x] == 1:
            return
        list[y][x] = 0
        self.dfs(list, m, n, y, x)

    def dfs(self, list: List, m: int, n: int, y: int, x: int):
        if y < 0 or x < 0 or y >= m or x >= n:
            return
        if list[y][x] == 0:
            list[y][x] = 1
            print('planted at', x, y, sep=' ')
            self.dfs(list, m, n, y - 1, x)
            self.dfs(list, m, n, y + 1, x)
            self.dfs(list, m, n, y, x - 1)
            self.dfs(list, m, n, y, x + 1)
            list[y][x] = 0

# sourcery skip: avoid-builtin-shadow
if __name__=="__main__":
    s = Solution()
    list = [[1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1]]
    s.plant_tree(list, 5, 5, 1, 1)