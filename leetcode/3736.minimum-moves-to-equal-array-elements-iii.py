# @lc app=leetcode id=3736 slug=minimum-moves-to-equal-array-elements-iii lang=python3
#
# [3736] Minimum Moves to Equal Array Elements III
# Difficulty: Easy
# Tags: Array, Math
# URL: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
#
# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)
        result = 0

        for num in nums:
            result += target - num
        return result
        

# @lc code=end
