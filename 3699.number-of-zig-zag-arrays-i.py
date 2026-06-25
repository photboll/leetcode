#
# @lc app=leetcode id=3699 lang=python3
#
# [3699] Number of ZigZag Arrays I
#

# @lc code=start
MOD = pow(10, 9) + 7
UP = 1
DOWN = 0

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        #number of values to choose from 
        m = r - l + 1
        dp = [1] * m

        for _ in range(2, n+1):
            dp.reverse()
            s = 0

            for j in range(m):
                dp[j], s = s, (s + dp[j]) % MOD
        
        return (sum(dp) % MOD << 1) % MOD




        
# @lc code=end

