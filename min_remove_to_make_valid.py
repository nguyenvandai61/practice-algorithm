class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                if stack:
                    stack.pop()
                else:
                    s=s[:i]+s[i+1:]
        for i in stack:
            s=s[:i]+s[i+1:]
        return s
        
if __name__ == "__main__":
    s = Solution()
    print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(s.minRemoveToMakeValid("a)b(c)d"))
    print(s.minRemoveToMakeValid("))(("))
    
    