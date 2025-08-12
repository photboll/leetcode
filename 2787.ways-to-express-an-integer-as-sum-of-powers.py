#
# @lc app=leetcode id=2787 lang=python3
#
# [2787] Ways to Express an Integer as Sum of Powers
#

# @lc code=start

MOD = pow(10, 9) + 7
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            val = i ** x
            for j in range(n+1):
                dp[i][j] = dp[i-1][j]
                if j >= val:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-val]) % MOD
        return dp[n][n]
        
# @lc code=end

