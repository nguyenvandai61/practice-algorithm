class Solutions:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = [ n for n in nums if n != 0]
        i = len(nums)
        while i < n:
            nums.append(0)
            i+=1
        return nums