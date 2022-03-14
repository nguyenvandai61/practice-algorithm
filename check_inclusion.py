"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
"""

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
       for i in range(s2):
         if s2[i] in s1:
           d = {}
           for j in range(s1):
            ch = s1[j]
                        
            
if __name__ == "__main__":
  s1 = "ab"
  s2 = "eidbaooo"
  sol = Solution()
  print(sol.check_inclusion(s1, s2))