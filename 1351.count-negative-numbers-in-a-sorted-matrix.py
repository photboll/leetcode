#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0
        r = m-1
        c = 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                res += n - c
                r -= 1
            else:
                c += 1
        
        return res
        
# @lc code=end

