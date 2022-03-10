from typing import List


class Solution:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]
      
if __name__ == "__main__":
    s = Solution()
    print(s.min_cost_climbing_stairs([10, 15, 20]))