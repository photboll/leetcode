#
# @lc app=leetcode id=3487 lang=python3
#
# [3487] Maximum Unique Subarray Sum After Deletion
#

# @lc code=start
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 1:
            return max(nums)
        nums = filter(lambda x: x > 0, nums)
        #Wait cant we just remove all duplicates?
        return sum(list(set(nums)))
        
# @lc code=end

