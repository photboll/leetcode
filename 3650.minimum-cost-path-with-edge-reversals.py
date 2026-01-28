#
# @lc app=leetcode id=3650 lang=python3
#
# [3650] Minimum Cost Path with Edge Reversals
#

# @lc code=start
from heapq import heappush, heappop, heapify
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        """   
        Do we need to keep track if we have used the reversal or not?
        No, since we only traverse each node once we can never walk from u twicr
        """
        neighbors = defaultdict(list)

        for u, v, w in edges:
            neighbors[u].append((v, w))
            neighbors[v].append((u, 2 * w))

        dist = [float("inf")]*n
        pq = [(0, 0)]

        while pq:
            curr_dist, curr= heappop(pq)
            if curr_dist > dist[curr]:
                continue
                
            if curr == n-1:
                return dist
            for neigh, weight in neighbors[curr]:
                new_dist = curr_dist + weight
                if new_dist < dist[neigh]:
                    dist[neigh] = new_dist
                    heappush(pq, (new_dist, neigh))
            
        return -1

        
# @lc code=end

