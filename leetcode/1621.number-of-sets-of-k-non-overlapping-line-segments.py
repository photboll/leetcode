# @lc app=leetcode id=1621 slug=number-of-sets-of-k-non-overlapping-line-segments lang=python3
#
# [1621] Number of Sets of K Non-Overlapping Line Segments
# Difficulty: Medium
# Tags: Math, Dynamic Programming, Combinatorics, Prefix Sum
# URL: https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
#
# @lc code=start
MOD = pow(10, 9) + 7

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        #dp[i][j] is the number of valid ways to construct i line segments using the points in [0, j]
        dp = [1] * n

        pref_sums = [0] * (n+1)

        for j in range(n):
             pref_sums[j+1] = (pref_sums[j] + dp[j]) % MOD

        for _ in range(k):
            dp[0] = 0
            for j in range(1, n):
                dp[j] = (dp[j-1] + pref_sums[j]) % MOD
            for j in range(n):
                pref_sums[j+1] = (pref_sums[j] + dp[j]) % MOD
        
        return dp[n-1]

    
            
        
        


        

        


# @lc code=end
