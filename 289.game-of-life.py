#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
DIRECTIONS = [(0,1), (1, 0), (0, -1), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]
def within_bounds(num_rows, num_cols, row, col):
    return (0 <= row < num_rows and 0<= col < num_cols)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        live_neighbors = [[0]*n for _ in range(m)]  
        #1. Find what will happen with each cell 
        for i in range(m):
            for j in range(n):
                count_live = 0
                for di, dj in DIRECTIONS:
                    ni, nj = i + di, j+dj
                    if within_bounds(m, n, ni, nj) and board[ni][nj] == 1:
                        count_live +=1
                live_neighbors[i][j] = count_live
        
        #2. update each cell accoring to the four rules
        for i in range(m):
            for j in range(n):
                cur_state = board[i][j]
                cur_count = live_neighbors[i][j]
                if cur_state == 0:
                    #Rule 4
                    #we only get new life when any cell have exactly 3 living neighbors
                    if cur_count == 3:
                        board[i][j] = 1
                    continue
                #Elese the cell is alive
                #Rule 1 & 3
                if cur_count == 2 or cur_count == 3:
                    board[i][j] = 1
                else:
                    #Rule 1 &  3
                    board[i][j] = 0
                
        
# @lc code=end

