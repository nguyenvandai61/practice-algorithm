from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if (len(pushed) != len(popped)):
            return False
        stack = []
        n = len(pushed)
        i = 0
        j = 0
        k = -1
        while i < n or j < n:
            print('i:', i, 'j:', j, 'k:', k, 'stack:', stack)
            if not stack:
                stack.append(pushed[i])
                k+=1
                i+=1
            elif stack[k] == popped[j]:
                stack.pop()
                k-=1
                j+=1
            else:
                if i == n:
                    return False
                stack.append(pushed[i])
                k+=1
                i+=1
            
        return not stack


if __name__=='__main__':
    s = Solution()
    print(s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
    print(s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
    print(s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2,6]))
   