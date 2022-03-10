class Solution:
  def is_subsequence(self, s: str, t: str) -> bool:
    if not s:
      return True
    if not t:
      return False
    if s[0] == t[0]:
      return self.is_subsequence(s[1:], t[1:])
    return self.is_subsequence(s, t[1:])
  
print(Solution().is_subsequence("abc", "ahbgdc"))