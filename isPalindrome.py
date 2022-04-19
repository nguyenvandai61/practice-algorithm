class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase
        alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()
        # delete all non-alpha char
        s = ''.join(c for c in s if c in alpha)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


if __name__=='__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))

        