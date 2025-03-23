#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def edgesToGraph(self, edges, succProb):
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
            
        return graph
    
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = self.edgesToGraph(edges, succProb)
        
        bestProb = [float("inf")]* n
        bestProb[start_node] = -1.0#The start node is guaranteed to be reachable 

        pq = [(-1.0, start_node)]#Negative values since heap is a min heap
        
        while pq:
            currProb, curr  = heappop(pq)
            if currProb < bestProb[curr]:
                continue
            
            for next, succesProb in graph[curr]:
                nextProb = currProb * succesProb
                if nextProb < bestProb[next]:
                    bestProb[next] = nextProb
                    heappush(pq, (nextProb, next))
                
        if bestProb[end_node] == float("inf"):
            return 0.0
        
        return -bestProb[end_node]
        
        
        
# @lc code=end

