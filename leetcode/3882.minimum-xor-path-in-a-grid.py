# @lc app=leetcode id=3882 slug=minimum-xor-path-in-a-grid lang=python3
#
# [3882] Minimum XOR Path in a Grid
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Bit Manipulation, Matrix
# URL: https://leetcode.com/problems/minimum-xor-path-in-a-grid/
#
# @lc code=start
MAX_VAL = 1024
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        #dp[i][j][x] = True means it is possible to reach value X at i,j
        dp = [[[False]*MAX_VAL for _ in range(n)] for _ in range(m)]

        #print(dp)

        #init
        dp[0][0][grid[0][0]] = True
        x = grid[0][0]
        for i in range(1, m):
            x = grid[i][0] ^ x
            dp[i][0][x] = True
        
        x = grid[0][0]
        for j in range(1, n):
            x = grid[0][j] ^ x
            dp[0][j][x] = True
        
        
        for i in range(1, m):
            for j in range(1, n):
                for k in range(MAX_VAL):
                    #Above
                    if dp[i-1][j][k]:
                        dp[i][j][k ^ grid[i][j]] = True

                    #Left
                    if dp[i][j-1][k]:
                        dp[i][j][k ^ grid[i][j]] = True
        
        return dp[-1][-1].index(True)

            

        

# @lc code=end
