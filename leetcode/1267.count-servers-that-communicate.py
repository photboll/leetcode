# @lc app=leetcode id=1267 slug=count-servers-that-communicate lang=python3
#
# [1267] Count Servers that Communicate
# Difficulty: Medium
# Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting
# URL: https://leetcode.com/problems/count-servers-that-communicate/
#
# @lc code=start
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        result = 0
        cols = [0] * n


        for r in range(m):
            for c in range(n):
                rows[r] += grid[r][c] 
                cols[c] += grid[r][c]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if rows[r] > 1 or cols[c] > 1:
                        result += 1
        return result

        
        

        
                
        

# @lc code=end
