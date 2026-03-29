#
# @lc app=leetcode id=3546 lang=python3
#
# [3546] Equal Sum Grid Partition I
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        row_sum = [0] * m
        col_sum = [0] * n 
        
        for r in range(m):
            for c in range(n):
                row_sum[r] += grid[r][c]
                col_sum[c] += grid[r][c]
        
        #print(row_sum, col_sum)
        tot_rows = sum(row_sum)
        s = 0
        for r in range(m):
            s += row_sum[r]
            if 2 * s == tot_rows:
                return True

        tot_cols = sum(col_sum)
        s = 0
        for c in range(c):
            s += col_sum[c]
            if 2 * s == tot_cols:
                return True

        return False

        
# @lc code=end

