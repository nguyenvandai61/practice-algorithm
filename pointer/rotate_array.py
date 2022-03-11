from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums 
      
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    
    print(s.rotate(nums, k))
        
    