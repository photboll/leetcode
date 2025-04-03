#
# @lc app=leetcode id=2908 lang=python3
#
# [2908] Minimum Sum of Mountain Triplets I
#

# @lc code=start
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_mountain = float("inf")
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        min_mountain = min(min_mountain, nums[i] + nums[j] + nums[k])
            
        if min_mountain == float("inf"):
            return -1
        else:
            return min_mountain

        
# @lc code=end

