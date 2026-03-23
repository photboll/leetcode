#
# @lc app=leetcode id=3567 lang=python3
#
# [3567] Minimum Absolute Difference in Sliding Submatrix
#

# @lc code=start
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                elements = [grid[r][c] for r in range(i, i+k) for c in range(j, j+k)]

                temp = sorted(set(elements))

                if len(temp) <= 1:
                    res[i][j] = 0
                else:
                    res[i][j] = min(temp[x+1] - temp[x] for x in range(len(temp)-1))

        return res
                
# @lc code=end

