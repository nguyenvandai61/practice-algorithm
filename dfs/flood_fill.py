from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image
      
    def dfs(self, image, sr, sc, oldColor, newColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        if image[sr][sc] != oldColor:
            return
        image[sr][sc] = newColor
        self.dfs(image, sr - 1, sc, oldColor, newColor)
        self.dfs(image, sr + 1, sc, oldColor, newColor)
        self.dfs(image, sr, sc - 1, oldColor, newColor)
        self.dfs(image, sr, sc + 1, oldColor, newColor)
      
   

if __name__ == "__main__":
    s = Solution()
    print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
    print(s.floodFill([[0,0,0],[0,1,1]], 1, 1, 1))