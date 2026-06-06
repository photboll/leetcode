#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rightSum = sum(nums)
        leftSum = 0
        result = [0] * n
        for i in range(n):
            rightSum -= nums[i]
            result[i] = abs(leftSum - rightSum)
            leftSum += nums[i]
        return result
        
# @lc code=end

