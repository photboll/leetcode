#
# @lc app=leetcode id=3195 lang=python3
#
# [3195] Find the Minimum Area to Cover All Ones I
#

# @lc code=start
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        we need to know the lowest number row that contains a 1
        the highes number row which contains a 1
        and finally the leftmost and the rightmost 1
        
        """

        m = len(grid)
        n = len(grid[0])

        topmost = m
        botmost = 0
        leftmost = n
        rightmost = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    topmost = min(topmost, i)
                    botmost = max(botmost, i)
                    leftmost = min(leftmost, j)
                    rightmost = max(rightmost, j)
        
        #There are no 1s in the grid 
        if topmost > botmost:
            return 0

        return (botmost - topmost + 1) * (rightmost - leftmost + 1)

                
        
# @lc code=end

