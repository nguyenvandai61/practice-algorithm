from typing import List


class Solution:
  def longest_common_prefix(self, strs: List[str]) -> str:
    if not strs:
      return ""
    if len(strs) == 1:
      return strs[0]
    for i, letter_group in enumerate(zip(*strs)):
      print(letter_group)
      if len(set(letter_group)) > 1:
        return strs[0][:i]
    return min(strs)

      
if __name__ == '__main__':
  s = Solution()
  print(s.longest_common_prefix(["ab", "a"]))
  print(s.longest_common_prefix(["ab", "a", "a"]))
  print(s.longest_common_prefix(["abc", "abde", "abc"]))