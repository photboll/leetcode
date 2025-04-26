#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        consecutive_ones = 0
        result = 0
        for right in range(n):
            if nums[right] == 1:
                consecutive_ones += 1
                result = max(result, consecutive_ones)
            else:
                consecutive_ones = 0

        return result
                
        
# @lc code=end

