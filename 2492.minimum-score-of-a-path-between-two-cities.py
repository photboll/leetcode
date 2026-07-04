#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

from heapq import heappush, heappop
from collections import defaultdict

# @lc code=start
class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        """
        it is allowed for apth to contain the same road multiple times, and you can visit the same city multiple times.
        How would this be useful? because we do not care about the toal distance at all.
        so we can take a very large detour in order to traverse the minimum road

        will the answer not simply be the shortest distance in the connected component that contains 1 and n?
        
        """
        
        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        result = float("inf")
        q = [1]
        visited = set()# keeps track of all edges
        seen_nodes = set() # keeps track of all nodes 

        while q:
            curr = q.pop()

            for neigh, dist in graph[curr]:
                edge = (curr, neigh) if curr < neigh else (neigh, curr)
                if edge in visited:
                    continue

                visited.add(edge)
                result = min(result, dist)

                if neigh not in seen_nodes:
                    seen_nodes.add(neigh)
                    q.append(neigh)

        return result
                    
                

if __name__ == "__main__":
    n = 4
    roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
    sol = Solution()
    #print(sol.minScore(n, roads))
    n = 14
    roads = [[12,7,2151],[7,2,7116],[11,14,8450],[11,2,9954],[1,11,3307],[10,7,3561],[10,1,4986],[11,7,7674],[14,2,1764],[11,12,6608],[14,7,1070],[9,8,2287],[14,12,6559],[1,2,1450],[2,12,9165]]
    print(sol.minScore(n, roads))

        



        
# @lc code=end

