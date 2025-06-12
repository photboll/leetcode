#
# @lc app=leetcode id=3423 lang=python3
#
# [3423] Maximum Difference Between Adjacent Elements in a Circular Array
#

# @lc code=start
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = abs(nums[-1] - nums[0])
        for i in range(1, len(nums)):
            max_diff = max(max_diff, abs(nums[i] - nums[i-1]))
            
        return max_diff
# @lc code=end

