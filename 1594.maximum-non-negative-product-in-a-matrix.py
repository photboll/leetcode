#
# @lc app=leetcode id=1594 lang=python3
#
# [1594] Maximum Non Negative Product in a Matrix
#

# @lc code=start
MOD = pow(10, 9) + 7
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[0]*2 for _ in range(n)] for _ in range(m)]
        p = dp[0][0][0] = dp[0][0][1] = grid[0][0]

        for c in range(1, n):
            p *= grid[0][c]
            dp[0][c][0] = p
            dp[0][c][1] = p
        
        p = grid[0][0]
        for r in range(1, m):
            p *= grid[r][0]
            dp[r][0][0] = p
            dp[r][0][1] = p

            for c in range(1, n):
                x = grid[r][c]
                candidates = (x * dp[r][c-1][0],
                              x * dp[r][c-1][1], 
                              x * dp[r-1][c][0], 
                              x * dp[r-1][c][1])
                
                dp[r][c][0] = min(candidates)
                dp[r][c][1] = max(candidates)
        result = dp[m-1][n-1][1]
        return -1 if result < 0 else result % MOD


        



        
# @lc code=end

