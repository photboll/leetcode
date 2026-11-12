# @lc app=leetcode id=3105 slug=longest-strictly-increasing-or-strictly-decreasing-subarray lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
# Difficulty: Easy
# Tags: Array
# URL: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
#
# @lc code=start
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # nums[:1] is always a valid answer with length 1
        increasing = 1
        decreasing = 1
        result = 1

        for i in range(1, n):

            if nums[i] > nums[i-1]:
                increasing += 1
            else:
                increasing = 1
            
            if nums[i] < nums[i-1]:
                decreasing += 1
            else:
                decreasing = 1
            
            result = max(result, increasing, decreasing)

        return result

            
                



        

# @lc code=end
