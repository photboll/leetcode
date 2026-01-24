#
# @lc app=leetcode id=1877 lang=python3
#
# [1877] Minimize Maximum Pair Sum in Array
#

# @lc code=start
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        res = 0

        for i in range(n//2):
            pair_sum = nums[i] + nums[n-1-i]
            res = max(res, pair_sum)
        return res
            
        
# @lc code=end

