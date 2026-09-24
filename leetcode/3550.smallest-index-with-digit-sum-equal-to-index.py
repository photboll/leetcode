# @lc app=leetcode id=3550 slug=smallest-index-with-digit-sum-equal-to-index lang=python3
#
# [3550] Smallest Index With Digit Sum Equal to Index
# Difficulty: Easy
# Tags: Array, Math
# URL: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
#
# @lc code=start
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(x):
            s = 0
            while x > 0:
                x, rem = divmod(x, 10)
                s += rem
            return s 
        
        for i, num in enumerate(nums):
            if i == digit_sum(num):
                return i

        return -1

# @lc code=end
