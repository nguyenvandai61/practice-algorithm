from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = 0
        n = len(nums)-1
        p = int((m+n)/2)
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        while(m<n-1):
            if nums[p] == target:
                return p
            elif nums[p] > target:
                n = p+1
            else:
                m = p+1
            p = int((m+n)/2)
            print(m,n,p)
        return -1
      
if __name__ == "__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 2))
    print(s.search([5], 5))
    print(s.search([2, 5], 5))
    