class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        i = 0
        s = list(s)
        print(s)
        while i < len(s):
            if s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
            elif s[i] == '(':
                stack.append(i)
            i += 1
        for i in stack:
            s[i] = ''
        return ''.join(s)
        
if __name__ == "__main__":
    s = Solution()
    print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(s.minRemoveToMakeValid("a)b(c)d"))
    print(s.minRemoveToMakeValid("))(("))
    
    