#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from collections import defaultdict

            
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = defaultdict(set)#key row number, values elements seen so far in this row
        seenCol = defaultdict(set)#key col number, values elements seen so far in this col
        seenBox = defaultdict(set)#key (subgrid_row, subgrid_col), values elements seen so far in this subgrid
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur_digit = board[i][j]
                if cur_digit == ".":
                    continue
                subBoxRow = i // 3
                subBoxCol = j // 3
                if cur_digit in seenRow[i] or cur_digit in seenCol[j] or cur_digit in seenBox[(subBoxRow, subBoxCol)]:
                    return False
                seenRow[i].add(cur_digit)
                seenCol[j].add(cur_digit)
                seenBox[(subBoxRow, subBoxCol)].add(cur_digit)
        
        return True
# @lc code=end

