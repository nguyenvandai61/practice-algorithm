from typing import List


class Solution:
  def max_sum_subarray(self, nums: List[int]) -> int:
    if len(nums) <= 1:
      return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
      dp[i] = max(dp[i-1] + nums[i] + nums[i-1], nums[i])
    return max(dp)
  

if __name__ == "__main__":
  s = Solution()
  print(s.max_sum_subarray([1, 2, -3, 4, 5]))