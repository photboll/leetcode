#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        N = m * n
        k %= N

        visited = 0
        start = 0

        while visited < N:
            current = start
            prev = grid[current // n][current % n]

            while True:
                nxt = (current + k) % N

                r, c = divmod(nxt, n)
                grid[r][c], prev = prev, grid[r][c]

                current = nxt
                visited += 1

                if current == start:
                    break

            start += 1

        return grid



        
# @lc code=end

