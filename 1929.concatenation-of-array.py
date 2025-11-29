#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        res.extend(nums)
        res.extend(nums)
        return res
        
# @lc code=end

