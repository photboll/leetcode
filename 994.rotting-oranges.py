#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
def within_bounds(m, n, r, c):
    return 0 <= r < m and 0<= c < n

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque() #(time, i, j, num_rotten)
        fresh_count = [0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count[0] += 1
                elif grid[i][j] == 2:
                    q.append((0, i, j))
        if fresh_count[0] == 0:
            return 0

        while q:
            time,i, j = q.popleft()

            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj
                if within_bounds(m, n, ni, nj) and grid[ni][nj] == 1:
                    fresh_count[0] -= 1
                    grid[ni][nj] = 2
                    q.append((time+1, ni, nj))
                    if fresh_count[0] == 0:
                        return time + 1
        return -1
# @lc code=end

