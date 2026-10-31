# @lc app=leetcode id=3665 slug=twisted-mirror-path-count lang=python3
#
# [3665] Twisted Mirror Path Count
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Matrix
# URL: https://leetcode.com/problems/twisted-mirror-path-count/
#
# @lc code=start
DOWN = (1, 0)
RIGHT =(0, 1)
DIRECTIONS = (DOWN, RIGHT)
MOD = pow(10, 9) + 7
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = {}

        def move(x, y, direction):
            nx = x + direction[0]
            ny = y + direction[1]
            if not (0 <= nx < m and 0 <= ny < n): 
                return None, None
            
            if grid[nx][ny] == 1:
                if direction == DOWN:
                    return move(nx, ny, RIGHT)
                else:
                    return move(nx, ny, DOWN) 
            return nx, ny
                
            
            
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
            

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                for dir in DIRECTIONS:
                    ni, nj = move(i, j, dir)

                    if ni is not None:
                        dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD
        
        return dp[-1][-1]
        

                    

        

# @lc code=end
