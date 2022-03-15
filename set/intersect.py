from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        res = a.intersection(b)
        return list(res)
      
if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1,2,2,1], [2,2]))