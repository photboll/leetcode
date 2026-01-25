#
# @lc app=leetcode id=1984 lang=python3
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#

# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = nums[k-1] - nums[0]
        for i in range(len(nums) - k+1):
            result = min(nums[i+k-1] - nums[i], result)
        return result

        
# @lc code=end
