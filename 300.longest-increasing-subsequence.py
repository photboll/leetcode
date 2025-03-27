#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp holds the length of the LIS ending at i
        #Initially all are 1 since any arr with only one elemet is increasing
        dp = [1] *len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # if element at i is increascing compared to the  element at j
                    #Then we can make that sequence 1 longer by adding the current element i to it
                    dp[i] =  max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

