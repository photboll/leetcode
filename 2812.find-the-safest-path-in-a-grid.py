#
# @lc app=leetcode id=2812 lang=python3
#
# [2812] Find the Safest Path in a Grid
#

# @lc code=start
from collections import deque
from heapq import heappop, heappush
DIRECTIONS = [(0,1), (0, -1), (1,0), (-1, 0)]

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            v = grid[i][j]
            
            for dx, dy in DIRECTIONS:
                x = i + dx
                y = j + dy

                if min(x, y) >= 0 and max(x, y) < n  and not grid[x][y]:
                    grid[x][y] = v + 1
                    q.append((x, y))
        
        pq = [(-grid[0][0], 0, 0)]

        while pq:
            safe, i , j = heappop(pq)
            safe = -safe

            if i == n-1 and j == n-1:
                return safe -1
            
            for dx, dy in DIRECTIONS:
                x, y = i + dx, j + dy

                if min(x, y) >= 0 and max(x, y) < n and grid[x][y] > 0:
                    heappush(pq, (-min(safe, grid[x][y], x, y)))
                    grid[x][y] *= -1
            
        return grid[n-1][n-1] - 1
            
                

        
# @lc code=end

