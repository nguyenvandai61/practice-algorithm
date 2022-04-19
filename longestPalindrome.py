class Solution:
    def doOdd(self, s: str, i: int, k: int):
        if i - k >= 0 and i + k < len(s) and s[i - k] == s[i + k]:
            k += 1
            return self.doOdd(s, i, k)
        else:
            return k-1

    def doEven(self, s: str, i: int, k: int):
        if i - k >= 0 and i + k + 1 < len(s) and s[i - k] == s[i + k + 1]:
            k += 1
            return self.doEven(s, i, k)
        else:
            return k
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        max_len = 1
        max_str = s[0]
        a = [0] * len(s)
        for i in range(len(s)):
            print('i:',i)

            k1 = self.doOdd(s, i, 0)
            print('k1:',k1)
            if k1*2+1 > max_len:
                max_len = k1*2+1
                print('i-k1+1:',i-k1+1)
                print('i+k1+1:',i+k1+1)
                max_str = s[i-k1:i+k1+1]
                print('max_str '+max_str)

            k2 = self.doEven(s, i, 0)
            print('k2:',k2)
            
            if k2*2 > max_len:
                max_len = k2*2
                max_str = s[i-k2+1:i+k2+1]
        print('max_len', max_len)
        return max_str
        


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('cbbd'))