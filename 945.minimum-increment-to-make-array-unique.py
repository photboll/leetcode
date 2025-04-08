#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        num_inc = 0
        for i in range(1,len(nums)):
            if nums[i-1] - nums[i] >= 0:
                diff = nums[i-1] - nums[i]
                num_inc += diff + 1
                nums[i] += diff + 1
        return num_inc
            
            
# @lc code=end

