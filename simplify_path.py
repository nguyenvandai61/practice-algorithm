class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p in ('', '.'):
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/home/"))
    print(s.simplifyPath("/a/./b/../../c/"))