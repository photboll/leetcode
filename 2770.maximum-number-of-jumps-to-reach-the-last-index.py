#
# @lc app=leetcode id=2770 lang=python3
#
# [2770] Maximum Number of Jumps to Reach the Last Index
#

# @lc code=start
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        """
        classic dp proble. where dp[i] is the maximum number of jumps to reach that position
        0 <= i < j < n we can only move forward
        
        """
        n = len(nums)

        dp = [-99999] * n
        dp[0] = 0

        for j in range(1, n):
            for i in range(j):
                #is it allwoed to jump from i to j?
                if abs(nums[j] - nums[i]) <= target:

                    dp[j] = max(dp[j], #keep the current best
                                dp[i] + 1 # ... -> i -> j
                                )
        return -1 if dp[-1] <= 0 else dp[-1]


        
# @lc code=end

