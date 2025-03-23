#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] *n for _ in range(n)]
        res = []
        #Which cols are occupied
        cols = [False] * n
        
        #Which diagonals are occupied both TooLEft to bottom right and bottom left to top right 
        #Main diagonals have row - col constant in span [-n + 1, n) <=> row - col + n in [1, 2n)
        #Anti-diagonals have row + col constant in span [0, 2n - 1)
        mainDiag = [False] * (2*n + 1)
        antiDiag = [False] * (2*n + 1)
        
        def backtrack(row):
            if row == n:
                #We have managed to place n queens in the grid
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                ##if can't place continue 
                if cols[col] or mainDiag[col - row + n] or antiDiag[col + row]:
                    #can not place if col or any of the diagonals are alreaddy occupied 
                    continue
                
                #Try to place at col
                #Place queen 
                board[row][col] = "Q"
                cols[col] = True
                mainDiag[col - row + n] = True
                antiDiag[col+row] = True
                
                #Try to continue solution by filling in the next row
                backtrack(row + 1)
                
                #Backtrackremove the queen 
                board[row][col] = "."
                cols[col] = False
                mainDiag[col - row + n] = False
                antiDiag[col+row] = False
        
        backtrack(0)
        return res
# @lc code=end

