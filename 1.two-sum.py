#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(len(nums)):
            if nums[i] in complement:
                return complement[nums[i]], i
            
            complement[target - nums[i]] = i
# @lc code=end

