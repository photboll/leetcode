#
# @lc app=leetcode id=2503 lang=python3
#
# [2503] Maximum Number of Points From Grid Queries
#

# @lc code=start
from heapq import heappush, heappop
def withinBounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])
DIRECTIONS = [(0, 1),#RIGHT 
              (1, 0),#DOWN 
              (0, -1),#LEFT
              (-1, 0)#UP
              ]
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        #The problem seems to be asking us to find for each query the size of each connected component,
        #That can be reached when starting from the top left corner. The connection criteria is that the queried value is strictly greater than each value in the cells 
        #Since we can revisit each cell multiples times, there is no risk of us getting stuck in a dead end 
        #This also any cell that is reachable from the starting cell will be visited. The order of visits are irrelevant to the total points 
        #We only get a point on the frist visit to each cell(for each query), so the total points will be the same as the size 
        #of the connected component
        
        #This solution hit TLE, I can not redo the entire BFS for each query 
        #We simply traverse the connected component in a DF manner (or BF) does not matter which, since we can revisit
        #If the start location does not give any points then we can't do anythng at all 
        sortedQueries = sorted(enumerate(queries), key=lambda x: x[1])
        answer = [0] * len(queries)

        heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0,0))

        count = 0
        qIndex = 0
        while heap:
            limit, iCurr, jCurr = heappop(heap)
            
            while qIndex < len(sortedQueries) and sortedQueries[qIndex][1] <= limit:
                answer[sortedQueries[qIndex][0]] = count 
                qIndex += 1
            
            count += 1
             
            for di, dj in DIRECTIONS:
                ni  = iCurr + di
                nj = jCurr + dj
                #we can acces a new previously unvisited cell that is within the limit 
                if withinBounds(grid, ni, nj) and (ni, nj) not in visited: 
                    visited.add((ni, nj))
                    heappush(heap, (grid[ni][nj], ni, nj))

        #Fill the remaining queries which all cover the entire grid
        while qIndex < len(sortedQueries):
            answer[sortedQueries[qIndex][0]] = count 
            qIndex += 1           
        return answer
# @lc code=end

