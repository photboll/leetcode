#
# @lc app=leetcode id=3651 lang=python3
#
# [3651] Minimum Cost Path with Teleportations
#

# @lc code=start
from functools import cache
def print_array(arr):
    for row in arr:
        print(row)

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        """   r
        dp, with the dp[r][c][l] = cost being the minimum cost to go from 0,0 to r, c with l teleportations    
        no probably better to do it teleportation level by level. 
        since teleporting l number of times requires that we only consdier the l-1 case
        
        
        """
        m = len(grid)
        n = len(grid[0])
        points = [(r, c) for r in range(m) for c in range(n)]
        points.sort(key= lambda p: grid[p[0]][p[1]])

        dp = [[float("inf")] * n for _ in range(m)]

        for _ in range(k+1):
            min_cost = float("inf")
            j = 0
            #With an additional teleport we can improve the min_cost 
            #of lesser points
            for i in range(len(points)):
                min_cost = min(min_cost,
                               dp[points[i][0]][points[i][1]]
                               )
                
                if (
                    i + 1 < len(points)
                    and grid[points[i][0]][points[i][1]]
                    == grid[points[i+1][0]][points[i+1][1]]
                ):
                    i += 1
                    continue

                for r in range(j, i+1):
                    dp[points[r][0]][points[r][1]] = min_cost
                    
                j = i+1
            
            #update dp array. after we have considered the additional teleport 
            for i in range(m-1, -1, -1):
                for j in range(n-1, -1, -1):
                    if i == m-1 and j== n-1:
                        dp[i][j] = 0
                        continue
                    
                    if i != m-1:
                        #move down
                        dp[i][j] = min(
                            dp[i][j],
                            dp[i+1][j] + grid[i+1][j]
                        )
                    if j != n-1:
                        #move left
                        dp[i][j] = min(
                            dp[i][j],
                            dp[i][j+1] + grid[i][j+1]
                        )

        return dp[0][0]




        
# @lc code=end

