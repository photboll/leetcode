#
# @lc app=leetcode id=3212 lang=python3
#
# [3212] Count Submatrices With Equal Frequency of X and Y
#

# @lc code=start
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        """
        similar to 3070.
        at least one "x".
        
        keep track of the counts of x and ys 
        """
        m = len(grid)
        n = len(grid[0])

        result = 0
        xCount = [0] * n
        yCount = [0] * n

        for r in range(m):
            curX = 0
            curY = 0
            for c in range(n):
                if grid[r][c] == "X":
                    xCount[c] += 1
                elif grid[r][c] == "Y":
                    yCount[c] += 1
                curY += yCount[c]
                curX += xCount[c]
                
                if curX == curY and curX > 0:
                    result += 1

                #print(r, c, curX, curY, result, xCount, yCount)
        return result
            
            
                
                
        
# @lc code=end

