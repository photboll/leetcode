#
# @lc app=leetcode id=2257 lang=python3
#
# [2257] Count Unguarded Cells in the Grid
#

# @lc code=start
from collections import deque
DIRECTIONS = [(0,1), (0, -1), (1, 0), (-1, 0)]
def within_bounds(i, j, m, n):
    return 0<= i < m and 0 <= j < n

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[""] * n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = "W"
        
        q = deque()
        for r, c in guards:
            grid[r][c] = "G"
            for dr, dc in DIRECTIONS:
                q.append((r, c, dr, dc))

        while q:
            r, c, dr, dc = q.popleft()

            nr = r + dr
            nc = c + dc
            #can we continue to move in this direciton
            if within_bounds(nr, nc, m, n) and\
                grid[nr][nc] not in ["W", "G"]:
                    grid[nr][nc] = "B"
                    q.append((nr, nc, dr, dc))
                    
        
        result = 0
        for r in range(m):
            for c in range(n):
                result += grid[r][c] == ""
                     
        return result



        
        

        
# @lc code=end

