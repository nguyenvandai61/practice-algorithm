class Solution:
    def valid_parenthese(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' or c == '}' or c == ']':
                if not stack:
                    return False
                if c == ')' and stack[-1] != '(':
                    return False
                if c == '}' and stack[-1] != '{':
                    return False
                if c == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        return not stack