#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
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
class SolutionV1:
    def maximumTripletValue(self, nums: List[int]) -> int:
       #Let start with doing th naive O(N**3) version
       maxVal = 0
       for i in range(len(nums)):
           for j in range(i+1, len(nums)):
               for k in range(j+1, len(nums)):
                   maxVal = max(maxVal, (nums[i]- nums[j])*nums[k])
       
       
       return maxVal 
# @lc code=end

