class Solution:
    def validPalindrome(self, s: str) -> bool:
        # after delete a char in string
        l = 0
        r = len(s) - 1
        c = 0
        l1 = 0
        r1 = len(s) - 1
        other = False
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if c == 1:
                    if not other and s[l1] == s[r1-1]:
                        l = l1
                        r = r1 - 1
                        c = 0
                        other = True
                    else:
                        return False              

                l1 = l
                r1 = r
                if s[l + 1] == s[r]:
                    l += 1
                elif s[l] == s[r - 1]:
                    r -= 1
                c += 1
        return True

if __name__=='__main__':
    s = Solution()
    print(s.validPalindrome("cuppucu"))
    print(s.validPalindrome("papaa"))
    print(s.validPalindrome("eeccccbebaeeabebccceea"))


