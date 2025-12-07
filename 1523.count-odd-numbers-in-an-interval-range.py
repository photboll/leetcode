#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = (high - low + 1) // 2
        res += (high % 2 == 1 == low % 2)
        return res
        
# @lc code=end

