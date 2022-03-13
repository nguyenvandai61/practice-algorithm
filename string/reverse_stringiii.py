class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        n = [x[::-1] for x in s]
        return ' '.join(n)
      
      
if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))