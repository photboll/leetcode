#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n#dp[i] Holds the size of the LDS of the subaray that ends at i 
        prev = [ -1 ] * n
        maxi = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    #Then adding nums[i] to the subset of dp[j] would be possible
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[maxi]:
                maxi = i
        result = []
        curr_i = maxi
        while curr_i > -1:
            result.append(nums[curr_i])
            curr_i = prev[curr_i]
        return result[::-1]
        
        
        
        
# @lc code=end