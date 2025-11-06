#
# @lc app=leetcode id=3607 lang=python3
#
# [3607] Power Grid Maintenance
#

# @lc code=start
from sortedcontainers import SortedList
from collections import defaultdict, deque
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)
        
        #BFS to find all connected components
        visited = set()       
        q = deque()
        stat2grid = {}        
        grid_i = 0
        grids = {}
        for station in range(1, c+1):
            if station in visited:
                continue
            cur_grid = SortedList()
            grids[grid_i] = cur_grid
            q.append(station)
            visited.add(station)

            while q:
                curr = q.popleft()
                stat2grid[curr] = grid_i
                cur_grid.add(curr)

                for neigh in edges[curr]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
            #Current connected component is completed 
            grid_i += 1
        
        #for k, v in grids.items():
        #   print(k, v)
        
        result = []
        #if station in visited then it is online
        for op, station in queries:
            if op == 2:
                grid = grids[stat2grid[station]]
                grid.discard(station)
                visited.discard(station)
            
            elif op == 1 and station in visited:
                result.append(station)
            elif op == 1:
                grid = grids[stat2grid[station]]
                result.append(grid[0] if len(grid) > 0 else -1)
        return result

            
        


            
            



            
            

        
        
        
        
        
# @lc code=end

