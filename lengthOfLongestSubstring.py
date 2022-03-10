class Solution:
  def length_of_longest_substring(self, s: str) -> int:
    if not s:
      return 0
    if len(s) == 1:
      return 1
    dp = [0] * len(s)
    dp[0] = 1
    # iterate through the string
    for i in range(1, len(s)):
      dp[i] = 1
      for j in range(i-dp[i-1], i):
        if s[i] == s[j]:
          dp[i] = i - j 
          break
        else:
          dp[i] = dp[i-1] + 1
    return max(dp)

print(Solution().length_of_longest_substring("abcabcbb"))
print('-----------------')
print(Solution().length_of_longest_substring("bbbbb"))
print('-----------------')
print(Solution().length_of_longest_substring("pwwkew"))