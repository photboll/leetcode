#
# @lc app=leetcode id=3446 lang=python3
#
# [3446] Sort Matrix by Diagonals
#

# @lc code=start
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        bot_left_diags_starts = [ (i, 0) for i in range(m)]
        top_right_diags_starts = [(0, j) for j in range(1, n)]
        
        def sort_diags(start_pos, reverse=True):
            for r, c in start_pos:
                #Gather all elements on this diagonal 
                cur_diag = []
                i, j = r, c
                while i < m and j < n:
                    cur_diag.append(grid[i][j])
                    i += 1
                    j += 1
                #Sort them
                cur_diag.sort(reverse=reverse)
                #Place them back 
                i, j = r, c
                for val in cur_diag:
                    grid[i][j] = val
                    i += 1
                    j += 1
                
        sort_diags(bot_left_diags_starts, reverse=True)
        sort_diags(top_right_diags_starts, reverse=False)
        
        
        return grid 


                
                
            
            
        
        
        
        
# @lc code=end

