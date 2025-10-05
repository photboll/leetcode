#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from collections import deque
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def within_bounds(m, n, r, c):
    return (0 <= r < m) and (0 <= c < n) 

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        BFS: 
        Should we walk uphilll from the oceans or downhill
        The issue with walking downhill is that we would need to keep track of the path down 
        as we do not know if it has reached the ocean until we arrive
        if i walk uphill i can just two rounds of bfs, one starting from atlantic and one from pacific
        if both walks traverses a cell then it should be added to the cell
        """
        m = len(heights)
        n = len(heights[0])
        visited = [[0] * n for _ in range(m)]

        ATLANTIC = 0b01
        PACIFIC = 0b10 
        REACHES_BOTH = ATLANTIC | PACIFIC

        def bfs(queue):
            while queue:
                r, c, ocean = queue.popleft()

                for dr, dc in DIRECTIONS:
                    nr = r + dr
                    nc = c + dc

                    #Can we walk to nr, nc?
                    if (within_bounds(m, n, nr, nc) 
                        and not (visited[nr][nc] & ocean)
                        and heights[nr][nc] >= heights[r][c]
                        ):
                        #Mark the current ocean as visited, and check if all conditions are satisfied
                        visited[nr][nc] |= ocean
                        queue.append((nr, nc, ocean))

        
        q = deque()
        #Starting points are all cells bordering an ocean 
        for r in range(m):
            visited[r][n-1] |= ATLANTIC
            q.append((r, n-1, ATLANTIC))
            visited[r][0] |= PACIFIC
            q.append((r, 0, PACIFIC))

        for c in range(n):
            visited[0][c] |= PACIFIC
            q.append((0, c, PACIFIC))
            visited[m-1][c] |= ATLANTIC
            q.append((m-1, c, ATLANTIC))
        
        def print_grid(grid):
            for row in grid:
                print(row)
        
        bfs(q)
        result = []
        for r in range(m):
            for c in range(n):
                if visited[r][c] == REACHES_BOTH:
                    result.append([r, c])
        
        
        return result



                            










        
        
# @lc code=end

