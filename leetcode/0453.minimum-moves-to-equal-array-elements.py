# @lc app=leetcode id=453 slug=minimum-moves-to-equal-array-elements lang=python3
#
# [453] Minimum Moves to Equal Array Elements
# Difficulty: Medium
# Tags: Array, Math
# URL: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
#
# @lc code=start
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        """
        should be the same as making them all equal where the operation is to subtract 1 form a single element 
        
        """
        n = len(nums)
        mn = min(nums)

        res = 0
        for num in nums:
            res += num - mn
        return res
        
        

# @lc code=end
