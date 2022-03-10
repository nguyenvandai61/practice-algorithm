class Solution:
    def nth_ugly_number(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [1]
        i2, i3, i5 = 0, 0, 0
        while len(dp) < n:
            min_val = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            if min_val == dp[i2] * 2:
                i2 += 1
            if min_val == dp[i3] * 3:
                i3 += 1
            if min_val == dp[i5] * 5:
                i5 += 1
            dp.append(min_val)
        return dp[-1]
        
            
if __name__ == "__main__":
    s = Solution()
    print(s.nth_ugly_number(15))