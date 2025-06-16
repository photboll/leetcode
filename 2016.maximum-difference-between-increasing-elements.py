#
# @lc app=leetcode id=2016 lang=python3
#
# [2016] Maximum Difference Between Increasing Elements
#

# @lc code=start
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = float("inf")
        max_diff = -1
        for num in nums:
            max_diff = max(max_diff, num-mn)
            mn = min(mn, num)
        if max_diff < 1:
            return -1
        
        return max_diff

            
        
# @lc code=end

