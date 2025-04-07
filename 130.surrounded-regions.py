#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
DIRECTIONS = [ (0, 1), (1, 0), (0, -1), (-1, 0)]
def withinBounds(m, n, i, j):
    return 0<= i < m and 0 <= j < n
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        is it enough that a region is not connected to an edge?
        since all cells are X XOR O it seems like it would be impossible to find a Region of Os that 
        does not touch the edge and is not surrounded.
        """
    
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfsRegion(i, j):
            touchesEdge = False
            indices = []
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                indices.append((x, y))

                #Is the current cell at the edge
                if x == 0 or y == 0 or x == m-1 or y == n-1:
                    touchesEdge = True
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y+ dy 
                    if withinBounds(m, n, nx, ny) and not visited[nx][ny] and board[nx][ny] == "O":
                        visited[nx][ny] = True
                        stack.append((nx, ny))
                    
            #We never came across an O at the edge 
            #This region is surrounded and should be changed to all Xs
            if not touchesEdge:
                for x, y in indices:
                    board[x][y] = "X"

                

        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" or visited[i][j]:
                    visited[i][j] = True
                    continue
                dfsRegion(i, j)
                
        
# @lc code=end

