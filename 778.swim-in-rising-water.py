#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
from heapq import heappush, heappop

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        pq = [(grid[0][0], 0, 0)]

        visited = set([(0,0 )])

        while pq:
            time, r, c = heappop(pq)

            if r == n-1 and c == n-1:
                return time
            
            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc

                if 0<= nr < n and 0<= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_time = max(time, grid[nr][nc])
                    heappush(pq, (new_time, nr, nc))

        



        
        
# @lc code=end

