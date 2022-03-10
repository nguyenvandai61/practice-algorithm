from typing import List


class Solution:
    def generate_pascal_triangle(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
            row.append(1)
            pascal_triangle.append(row)
        return pascal_triangle