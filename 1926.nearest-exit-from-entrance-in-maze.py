#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
def within_bounds(m, n, r, c):
    return 0 <= r < m and 0<= c < n

def is_exit(m, n, r, c, entrance):
    """The exit is any cell at the border of the maze that is not the same as the entrance"""
    if entrance[0] == r and entrance[1] == c:
        return False
    return r == 0 or r == m-1 or c== 0 or c == n-1
    

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        queue = deque()
        queue.append((0, entrance[0], entrance[1]))# (num_steps, row, col)
        maze[entrance[0]][entrance[1]] = "S"#mark the starting locations as used
         
        while queue:
            num_steps, curr_r, curr_c = queue.popleft()
            if is_exit(m, n, curr_r, curr_c, entrance):
                return num_steps
            
            for dr, dc in DIRECTIONS:
                nr, nc = curr_r + dr, curr_c + dc
                if within_bounds(m, n, nr, nc) and maze[nr][nc] == ".":
                    queue.append((num_steps+1, nr, nc))
                    maze[nr][nc] = "x"

        return -1

            
        


        
# @lc code=end

