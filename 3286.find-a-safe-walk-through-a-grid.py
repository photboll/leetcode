#
# @lc app=leetcode id=3286 lang=python3
#
# [3286] Find a Safe Walk Through a Grid
#

# @lc code=start
from heapq import *
DIRECTIONS = [(0,1), (0, -1), (1,0), (-1, 0)]

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        """
        dp or dijkstra?
        we only care about if we have at least 1 health 
        we do not have to maximize our final health 
        
        """
        m = len(grid)
        n = len(grid[0])

        #-health to make it a max heap
        #(-health, i, j)
        pq = [(-(health - grid[0][0]), 0, 0)]
        visited = set((0, 0))

        while pq:
            h, i, j = heappop(pq)
            h = -h
            if i  == m-1 and j == n-1:
                return h > 0

            for di, dj in DIRECTIONS:
                ni = i + di
                nj = j + dj
                if 0<= ni < m and 0<= nj < n:
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        heappush(pq, (-(h-grid[ni][nj]), ni, nj))

        return False
                        

            
if __name__ == "__main__":
    sol = Solution()
    print(sol.findSafeWalk([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 1))

        
# @lc code=end

