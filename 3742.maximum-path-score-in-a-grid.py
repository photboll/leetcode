#
# @lc app=leetcode id=3742 lang=python3
#
# [3742] Maximum Path Score in a Grid
#

# @lc code=start
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        m = len(grid)
        n = len(grid[0])
        #dp[i][j][c] maximum score that can be achieved at i, j with exactly c costs
        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                for cost in range(k+1):
                    new_cost = cost + 1 if grid[i][j] > 0 else cost
                    if new_cost > k:
                        continue

                    if i == m-1 and j == n-1:
                        dp[i][j][cost] = grid[i][j]
                        continue

                    best_next = max(
                        dp[i+1][j][new_cost] if i + 1  <  m else -1,
                        dp[i][j+1][new_cost] if j + 1 < n else -1
                    )

                    if best_next > -1:
                        dp[i][j][cost] = grid[i][j] + best_next

        return dp[0][0][0]


                
                
        
        
# @lc code=end

