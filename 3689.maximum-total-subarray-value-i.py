#
# @lc app=leetcode id=3689 lang=python3
#
# [3689] Maximum Total Subarray Value I
#

# @lc code=start
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)

        return k*(mx - mn)
        
# @lc code=end

