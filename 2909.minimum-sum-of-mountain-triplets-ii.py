#
# @lc app=leetcode id=2909 lang=python3
#
# [2909] Minimum Sum of Mountain Triplets II
#

# @lc code=start
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_min = [nums[0]]* n
        suffix_min = [nums[-1]] * n
        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i-1], nums[i])
            suffix_min[n - 1 - i] = min(suffix_min[n -i], nums[n -1 -i])

        min_mountain = float("inf")
        
        
        for i in range(1, n-1):
            if prefix_min[i-1] < nums[i] and suffix_min[i+1] < nums[i]:
                min_mountain = min(min_mountain, prefix_min[i-1] + nums[i] + suffix_min[i+1])
        
        if min_mountain == float("inf"):
            return -1
        
        else:
            return min_mountain
        
# @lc code=end

