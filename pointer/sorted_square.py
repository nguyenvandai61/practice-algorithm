from typing import List


class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        return sorted([n * n for n in nums])
      

if __name__== '__main__':
    s = Solution()
    nums = [-4,-1,0,3,10]
    print(s.sorted_squares(nums))