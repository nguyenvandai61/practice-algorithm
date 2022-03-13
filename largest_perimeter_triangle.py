from typing import List


class Solution:
    def largest_perimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        i = len(nums) - 1
        while i >= 2:
            if nums[i] + nums[i-1] <= nums[i-2]:
                i-= 1        
                continue
            if nums[i-1] + nums[i-2] <= nums[i]:
                i-= 1        
                continue
            if nums[i-2] + nums[i] <= nums[i-1]:
                i-= 1        
                continue
            return nums[i] + nums[i-1] + nums[i-2]
        return 0
      
      
if __name__ == "__main__":
    s = Solution()
    print(s.largest_perimeter([2, 1, 2]))
    print(s.largest_perimeter([1, 2, 1]))
    print(s.largest_perimeter([2,1,3,4]))
    print(s.largest_perimeter([3, 6, 2, 3]))
    print(s.largest_perimeter([1, 2, 1]))