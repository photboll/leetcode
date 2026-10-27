# @lc app=leetcode id=1254 slug=number-of-closed-islands lang=python3
#
# [1254] Number of Closed Islands
# Difficulty: Medium
# Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
# URL: https://leetcode.com/problems/number-of-closed-islands/
#
# @lc code=start


DIRECTIONS  = [(1,0), (-1, 0), (0, 1), (0,-1)]
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        closed_islands = 0
        stack = []
        visited = [[False]*n for _ in range(m)]

        
        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == 1:
                    continue

                # Current position is land 
                visited[i][j] = True
                stack.append((i, j))
                is_closed = True

                while stack:
                    cur_i, cur_j = stack.pop()

                    for di, dj in DIRECTIONS:
                        ni, nj = cur_i + di, cur_j + dj
                        #if we try to setp out of bounds
                        if not(0 <= ni < m and 0 <= nj < n):
                            is_closed = False
                        elif grid[ni][nj] == 0 and not visited[ni][nj]: #is land
                            visited[ni][nj] = True
                            stack.append((ni, nj))
                        
                        
                
                if is_closed:
                    closed_islands += 1
        
        return closed_islands






                
                
                


        

# @lc code=end
