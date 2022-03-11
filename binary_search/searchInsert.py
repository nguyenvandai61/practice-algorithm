class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        m = 0
        n = len(nums)-1
        p = (m+n)//2
        
        while m <= n:
            if nums[p+1] >= target and nums[p] < target:
                print(p)
                return p+1
            elif nums[p] < target:
                m = p+1
            else:
                n = p-1
            p = (m+n)//2