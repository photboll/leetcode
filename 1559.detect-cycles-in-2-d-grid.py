#
# @lc app=leetcode id=1559 lang=python3
#
# [1559] Detect Cycles in 2D Grid
#

# @lc code=start
from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

from collections import deque

class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                
                char = grid[i][j]
                queue = deque([((i, j), (-1, -1))])
                visited.add((i, j))
                
                while queue:
                    (ci, cj), (pi, pj) = queue.popleft()
                    
                    for di, dj in DIRECTIONS:
                        ni, nj = ci + di, cj + dj
                        
                        if 0 <= ni < m and 0 <= nj < n:
                            if grid[ni][nj] == char:
                                if (ni, nj) == (pi, pj):
                                    continue
                                
                                if (ni, nj) in visited:
                                    return True
                                
                                visited.add((ni, nj))
                                queue.append(((ni, nj), (ci, cj)))
                                
        return False



        
# @lc code=end

