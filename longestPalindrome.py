class Solution:
    def longest_palindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 0
        max_str = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        max_str = s[i:j+1]
        return max_str