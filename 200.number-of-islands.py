#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def within_bounds(m, n, i, j):
    return 0<= i < m and 0<= j < n

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = deque()
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                q.append((i, j))
                num_islands += 1
                while q:
                    k, l = q.popleft()
                    
                    for dk, dl in DIRECTIONS:
                        nk, nl = k + dk, l + dl
                        if within_bounds(m, n, nk, nl) and not visited[nk][nl]:
                            visited[nk][nl] = True
                            if grid[nk][nl] == "1":
                                q.append((nk, nl))

        return num_islands
        
# @lc code=end

