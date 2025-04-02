#
# @lc app=leetcode id=2874 lang=python3
#
# [2874] Maximum Value of an Ordered Triplet II
#

# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        maxTriplet = 0
        maxNum = nums[0]
        maxDiff = float("-inf")
        for j in range(1, len(nums)-1):
            maxDiff = max(maxDiff, maxNum - nums[j])
            maxTriplet = max(maxTriplet, maxDiff * nums[j+1])
            maxNum = max(maxNum, nums[j])
        return  max(maxTriplet, 0)
        
# @lc code=end

