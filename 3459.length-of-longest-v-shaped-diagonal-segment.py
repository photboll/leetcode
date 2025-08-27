#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
from functools import cache
DIRECTIONS = [(-1,-1), (-1, 1), (1, 1), (1, -1)]

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @cache
        def dfs(row, col, direction, can_turn, target):
            nrow = row + DIRECTIONS[direction][0]  
            ncol = col + DIRECTIONS[direction][1]
            
            #Makes sure we are in a valid state
            if nrow < 0 or ncol < 0 or nrow >= m or ncol >= n or grid[nrow][ncol] != target:
                return 0
            
            #We can either continue on in the same direction or possibly turn 
            max_v = dfs(nrow, ncol, direction, can_turn, 2 - target)
            if can_turn:
                max_v = max(max_v,
                            dfs(nrow, ncol, (direction + 1) % len(DIRECTIONS), False, 2 - target)
                            )
            
            return max_v + 1
        
        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dir in range(len(DIRECTIONS)):
                        res = max(res, 
                                dfs(i, j, dir, True, 2)+1
                                )
        return res 
                
                

        
# @lc code=end

