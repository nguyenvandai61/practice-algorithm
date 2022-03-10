from typing import List


class Solution:
    def find_lucky(self, nums: List[int]) -> int:
        c = {}
        for n in nums:
            if n in c:
                c[n]+=1
            else:
                c[n]=1
        luckys = [k for k, v in c.items() if k == v]
        return max(luckys, default=-1)
    
if __name__ == "__main__":
    s = Solution()
    print(s.find_lucky([2, 2, 3, 4]))
    print(s.find_lucky([2,2,2,3,3]))