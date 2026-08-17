#
# @lc app=leetcode id=3702 lang=python3
#
# [3702] Longest Subsequence With Non-Zero Bitwise XOR
#

# @lc code=start
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        all_zero = True
        for num in nums:
            total ^= num
            if num > 0:
                all_zero = False       
        if all_zero:
            return 0
        elif total:
            return len(nums)
        else:
            return len(nums)-1
# @lc code=end

