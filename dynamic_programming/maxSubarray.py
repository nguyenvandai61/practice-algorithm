from typing import List


def max_sub_array(nums: List[int]) -> int:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    """
    max_sum = nums[0]
    cur_sum = nums[0]
    for i in range(1, len(nums)):
        cur_sum = max(nums[i], cur_sum + nums[i])
        max_sum = max(max_sum, cur_sum)
    return max_sum
    


if __name__ == '__main__':
  nums = [-2,1,-3,4,-1,2,1,-5,4]
  print(max_sub_array(nums))
  
