from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        return nums1
      
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = []
        i=j=0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] >= nums2[j]:
                a.append(j)
                i+=1
            if nums1[i] < nums2[j]:
                a.append(i)
                j+=1
        a += nums1[i:]
        a += nums2[j:]
        nums1[:] = a
        return nums1