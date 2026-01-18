#
# @lc app=leetcode id=1895 lang=python3
#
# [1895] Largest Magic Square
#

# @lc code=start
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        def is_magic_square(grid, r, c, k):
            target = sum(grid[r][c:c+k])
            #Check Rows
            for i in range(r+1, r+k):
                curr = sum(grid[i][c:c+k])
                if curr != target:
                    return False

            
            #Check Cols
            for j in range(c, c+k):
                curr = 0
                for i in range(r, r+k):
                    curr += grid[i][j]
                if curr != target:
                    return False
            
            #Check diagonals
            main = 0
            anti = 0
            for i in range(k):
                main += grid[r+i][c+i]
                anti += grid[r+i][c+k-i]
            if main != target or anti!= target:
                return False
            return True
        
        m = len(grid)
        n = len(grid[0])

        for side_len in range(min(m, n), 0, -1):
            for row in range(0, m - side_len):
                for col in range(0, n-side_len):
                    if is_magic_square(grid, row, col, side_len):
                        return side_len
        return 1
        
# @lc code=end

