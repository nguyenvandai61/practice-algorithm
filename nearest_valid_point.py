from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float("inf")
        min_point = -1
        for i in range(len(points)):
            if points[i][0] != x and points[i][1] != y:
                continue
            distance = abs(points[i][0] - x) + abs(points[i][1] - y)
            if distance < min_distance:
                min_distance = distance
                min_point = i
        return min_point
      
if __name__ == "__main__":
    s = Solution()
    print(s.nearestValidPoint(1, 1, [[0,0],[0,2],[2,0],[2,2]]))
    print(s.nearestValidPoint(2, 3, [[0,0],[0,2],[2,0],[2,2]]))