#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        if self.solve_horizontal(grid):
            return True
        
        #Transpose to solve the vertical cuts
        transposed_grid = list(map(list, zip(*grid)))
        return self.solve_horizontal(transposed_grid)
    
    def solve_horizontal(self, grid):
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        
        # Frequency arrays for top and bottom partitions
        top_freq = [0] * 100001
        bot_freq = [0] * 100001

        for row in grid:
            for val in row:
                bot_freq[val] += 1

        curr_top_sum = 0
        for i in range(m -1):
            for j in range(n):
                val = grid[i][j]
                curr_top_sum += val
                top_freq[val] += 1
                bot_freq[val] -= 1
            
            curr_bot_sum = total - curr_top_sum
            if curr_top_sum == curr_bot_sum:
                return True
            
            diff = abs(curr_top_sum - curr_bot_sum)
            if diff <= 100000:
                if curr_top_sum > curr_bot_sum:
                    if self.check(top_freq, grid, 0, i, 0, n-1, diff):
                        return True
                    
                else:
                    if self.check(bot_freq, grid, i+1, m-1, 0, n-1, diff):
                        return True

        return False

        
    def check(self, freq, grid, r1, r2, c1, c2, diff):
        # check if the 
        rows = r2 -r1 + 1
        cols = c2 - c1 + 1

        if rows * cols == 1:
            return False
        
        #1D arrays then we can only remove the andpoints
        if rows == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff
        
        if cols == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff
        
        #2d are we can remove any of the values in the grid wihtout breaking the connectedness
        return freq[diff] > 0
        

        
# @lc code=end

