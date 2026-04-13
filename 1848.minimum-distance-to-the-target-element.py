#
# @lc app=leetcode id=1848 lang=python3
#
# [1848] Minimum Distance to the Target Element
#

# @lc code=start
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float("inf")

        for i in range(start, len(nums)):
            if nums[i] == target:
                res = min(res, abs(start-i))
                break
        
        for i in range(start, -1,-1):
            if nums[i] == target:
                res = min(res, abs(start-i))
                break
        return res
    
        
# @lc code=end

