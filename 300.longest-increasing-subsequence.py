#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size_LIS = 0
        n = len(nums)
        tails = [0]*n #Holds the smallest endning element of all increasing subsequence of length i+1
        for num in nums:
            i, j = 0, size_LIS
            #Binary search
            while i != j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            size_LIS = max(i+1, size_LIS)
        return size_LIS
            

class SolutionV1:
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

