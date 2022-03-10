from typing import List


def two_sum(self, nums: List[int], target: int) -> List[int]:
  c = {}
  for i, n in enumerate(nums):
    if target - n in c:
      return [c[target - n], i]
    c[n] = i
    
