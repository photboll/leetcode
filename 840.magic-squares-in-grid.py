#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#

# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def is_magic_square(grid, r, c):
            seen = [0] * 10
            
            for i in range(r, r+3):
                for j in range(c, c+3):
                    val = grid[i][j]
                    if val < 1 or val > 9 or seen[val]:
                        return False
                    seen[val] = 1
            
            # Row 1
            if grid[r][c] + grid[r][c + 1] + grid[r][c + 2] != 15: return False
            # Row 3
            if grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] != 15: return False
            
            # Col 1
            if grid[r][c] + grid[r + 1][c] + grid[r + 2][c] != 15: return False
            # Col 3
            if grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] != 15: return False
            
            # Diagonal 1
            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15: return False
            # Diagonal 2
            if grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2] != 15: return False
            
            return True

        cnt = 0
        m = len(grid)
        n = len(grid[0])
        for r in range(m-2):
            for c in range(n-2):
                if is_magic_square(grid, r, c):
                    cnt +=1
        return cnt
    
    
    
        
# @lc code=end

