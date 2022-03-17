from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [0] * len(prices)
        dp[0] = 0
        dp[1] = max(0, prices[1] - prices[0])
        for i in range(2, len(prices)):
            print(dp)
            dp[i] = max(0, prices[i] - prices[i - 1] + dp[i - 1])
        return max(dp)
      
      
if __name__=='__main__':
    s = Solution()
    print(s.maxProfit([1,7]))
    print(s.maxProfit([2,1,2,1,0,1,2]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([7,6,4,3,1]))
    print(s.maxProfit([1,2,4,2,5,7,2,4,9,0]))