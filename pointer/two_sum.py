from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(numbers):
            if n in d:
                return [d[n], i+1]
            else:
                d[target-n] = i+1
        return []
      
if __name__ == '__main__':
    s = Solution()
    nums = [2]
    target = 9
    print(s.two_sum(nums, target))