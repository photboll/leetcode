#
# @lc app=leetcode id=2976 lang=python3
#
# [2976] Minimum Cost to Convert String I
#

# @lc code=start
from heapq import heappush, heappop

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len(source) != len(target):
            return -1
        
        adj = [[] for _ in range(26)]
        for u, v, w in zip(original, changed, cost):
            adj[ord(u) - 97].append((ord(v) - 97, w))
        
        dist = [[float("inf")]*26 for _ in range(26)]
        
        def dijkstra(src):
            pq = [(0, src)]
            dist[src][src] = 0
            while pq:
                d, u = heappop(pq)
                if d > dist[src][u]:
                    continue

                for v, w in adj[u]:
                    if dist[src][v] > d+w:
                        dist[src][v] = d + w
                        heappush(pq, (dist[src][v], v))
        
        for i in range(26):
            dijkstra(i)

        result = 0

        for s, t in zip(source, target):
            u, v = ord(s) - 97, ord(t) - 97
            if u == v:
                continue
            if dist[u][v] == float("inf"):
                return -1
            result += dist[u][v]

        return result
            
        
        





            
        
# @lc code=end

