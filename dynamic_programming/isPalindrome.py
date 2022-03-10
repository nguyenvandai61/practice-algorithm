class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        revert = 0
        while x > revert: 
            revert = revert *10 +x%10
            x = int(x/10)
        return revert == x or int(revert/10) == x

    def is_palindrome_2(self, x: int) -> bool:
        if str(x)==str(x)[::-1] :
            return True 
          
if __name__ == "__main__":
    s = Solution()
    print(s.is_palindrome(121))            