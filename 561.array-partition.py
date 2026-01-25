#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0

        for i in range(len(nums)-1, -1, -2):
            result += min(nums[i], nums[i-1])
        return result
        
# @lc code=end

