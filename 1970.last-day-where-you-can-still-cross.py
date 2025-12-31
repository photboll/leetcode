#
# @lc app=leetcode id=1970 lang=python3
#
# [1970] Last Day Where You Can Still Cross
#

# @lc code=start
from heapq import heappush, heappop, heapify
DIRECTIONS = [(1,0), (0, 1), (-1, 0), (0, -1)]
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
        is it fast enough to binary search over the time index and simply build the grid
        and test if a path exists 
        """
        #chagne to 0 based indexing
        cells = [[a-1, b-1] for a, b in cells]

        def get_start_pos(grid):
            pos = []
            for c in range(len(grid[0])):
                if grid[0][c] == 0:
                    pos.append(c)
            return pos
        def within_bounds(r, c):
            return 0 <= r < row and 0<= c < col
            
            
        def can_cross(grid):
            #dijkstra to find if a path exists
            #we want to reach the last row, row -r is the distance to it 
            #row is a constant, using -r is enough 
            q = [(0, c) for c in get_start_pos(grid)]
            heapify(q)

            while q:
                r, c = heappop(q)
                r = -r#change from distance to index
                if r == row -1:# we have reached the other side
                    return True
                
                for dr, dc in DIRECTIONS:
                    nr = r + dr
                    nc = c + dc
                    #can only walk on land 
                    if within_bounds(nr, nc) and grid[nr][nc] == 0:
                    #modify grid to signify that we have visited a cell
                        grid[nr][nc] = 2
                        #-nr to prioritze cells that are closer to the end
                        heappush(q, (-nr, nc))
            return False

        def can_cross_at_t(t):
            grid = [[0] * col for _ in range(row)]
            for [r, c] in cells[:t]:
                grid[r][c] = 1
            res = can_cross(grid)
            #print(t, grid, res)
            return res
            
        
        #Binary search on the time
        low = 0
        high = len(cells)
        while low < high:
            mid = (low + high + 1) // 2

            if can_cross_at_t(mid):
                low = mid 
            else:
                high = mid -1

        return low




        
# @lc code=end

