#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from collections import deque
def flatten_boustrophedon_board(board):
    result = []
    should_reverse = False
    for i in range(len(board)-1, -1, -1):
        if should_reverse:
            result.extend(board[i][::-1])
        else:
            result.extend(board[i])
        should_reverse = not should_reverse
    return result

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        BFS on the grid positions we find the least number of moves that need to be used in order
        to move to each position.
        the boustrophedon style thing just jumbles the logic a bit.
        maybe i should jus flatten the entire board. since the shape of the board is only relevant for the design 
        not the logic of the game 
        """
        n = len(board)
        target = n * n -1 
        board = flatten_boustrophedon_board(board)
        queue = deque()
        queue.append((0, 0))#(position 0 indexed, num_steps to reach)
        visited = set()
        while queue:
            curr_pos, curr_steps = queue.popleft()
            if curr_pos == target:
                return curr_steps
            
            for step_size in range(1, 7):
                next_pos = min(curr_pos + step_size, target)
                if board[next_pos] > -1:
                    next_pos = board[next_pos] - 1#NOTE: The board uses 1-based indexing while we use 0

                if next_pos not in visited:
                    queue.append((next_pos, curr_steps + 1))
                    visited.add(next_pos)
            
        return -1
# @lc code=end

