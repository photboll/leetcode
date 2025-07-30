#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = 0
        result = 0
        curr_streak = 0
        
        for num in nums:
            if max_val < num:
                max_val = num
                result = 0
                curr_streak = 0
            
            if max_val == num:
                curr_streak += 1
            else:
                curr_streak = 0
            
            result = max(result, curr_streak)
        
        return result
        
# @lc code=end

