class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[1] = False
        dp[2] = True
        for i in range(3, n + 1):
            for j in range(1, i):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break
        return dp[n]