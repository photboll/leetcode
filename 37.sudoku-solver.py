#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from copy import deepcopy
from collections import defaultdict
from typing import List
import time
def get_subgrid_num(i, j):
    return 3*(i //3) + j //3

def init_seen(board): 
    seenRow = [set() for _ in range(9)]
    seenCol = [set() for _ in range(9)]
    seenBox = [set() for _ in range(9)]
    blankPositions = []
    
    for i in range(9):
        for j in range(9):
            cur_digit = board[i][j]
            if cur_digit == ".":
                blankPositions.append((i, j))
            else:
                seenRow[i].add(cur_digit)
                seenCol[j].add(cur_digit)
                seenBox[get_subgrid_num(i, j)].add(cur_digit)
                
    return seenRow, seenCol, seenBox, blankPositions

class SolutionV1:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seenRow, seenCol, seenBox, blankPositions = init_seen(board) 
        DIGITS = [str(i+1) for i in range(9)]
        def backtrack(index) :
            if len(blankPositions) == index:
                return True
            
            i, j = blankPositions[index]
            sub_grid = get_subgrid_num(i, j)
            for d in DIGITS:
                if d in seenRow[i] or d in seenCol[j] or d in seenBox[sub_grid]:
                    continue
                board[i][j] = d
                seenRow[i].add(d)
                seenCol[j].add(d)
                seenBox[sub_grid].add(d)
                
                if backtrack(index+1):
                    return True
                board[i][j] = "." #reset it if no solution was found 
                seenRow[i].remove(d)
                seenCol[j].remove(d)
                seenBox[sub_grid].remove(d)
            return False 
        backtrack(0)

class SolutionV2:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seenRow, seenCol, seenBox, blankPositions = init_seen(board) 
        DIGITS = {str(i + 1) for i in range(9)}
        
        # Sort positions based on possible choices (heuristic ordering)
        def get_choices(i, j):
            sub_grid = get_subgrid_num(i, j)
            return DIGITS - seenRow[i] - seenCol[j] - seenBox[sub_grid]
        
        blankPositions.sort(key=lambda pos: len(get_choices(*pos)))
        
        def backtrack(index):
            if index == len(blankPositions):
                return True  # All cells are filled
            
            i, j = blankPositions[index]
            box_index = get_subgrid_num(i, j)
            choices = DIGITS - seenRow[i] - seenCol[j] - seenBox[box_index]
            
            for d in choices:
                board[i][j] = d
                seenRow[i].add(d)
                seenCol[j].add(d)
                seenBox[box_index].add(d)
                
                if backtrack(index + 1):
                    return True
                
                # Backtrack
                board[i][j] = "."
                seenRow[i].remove(d)
                seenCol[j].remove(d)
                seenBox[box_index].remove(d)
            
            return False
        
        backtrack(0)

test_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# @lc code=end


def benchmark(solution_class, board):
    board_copy = deepcopy(board)
    solver = solution_class()
    start_time = time.time()
    solver.solveSudoku(board_copy)
    end_time = time.time()
    return end_time - start_time

# Run benchmark
v1_time = benchmark(SolutionV1, test_board)
v2_time = benchmark(SolutionV2, test_board)

print(f"V1 Execution Time: {v1_time:.6f} seconds")
print(f"V2 Execution Time: {v2_time:.6f} seconds")
