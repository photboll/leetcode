#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
from collections import defaultdict, deque
from heapq import heappop, heappush
class Solution:
    def pruneRoads(self, roads: List[List[int]], shortDist: List[int]):
        graph = defaultdict(list)
        inDegrees = defaultdict(int) 
        for u, v, w in roads:
            if shortDist[v] < shortDist[u]:
                #swap so that u is always the earliest node
                u, v = v, u
        
            if shortDist[u] + w == shortDist[v]:
                graph[u].append(v)
                inDegrees[v] += 1
                
        return graph, inDegrees
        
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #
        #1. We want to know what is the shortest path from 0 to every node x. shortDist 
        #2. We want to know Which edges (u, v, w) satsifies shortDist[u] + w == shortDist[v]
        #i.e. all roads which would equal the best route to each node [NOTE: biDirectionality]
        #This would prune out all edges which will never be in a best path.
        #The grph would become much sparser. Would it even become a DAG?
        #Yes. all roads will be forced to be directed since all weights are positive. They are times
        #If it contains a cycle, then traversing the cycle would only make the total travel time longer
        #So it can't possibly be part of a shorteest path. Since the path with the cycle cut out would be shorter
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))#The roads are bidirectional 
        
        shortDist = [float("inf")] * n
        shortDist[0] = 0
        heap = [(0, 0)]# (totalDist, node)
        while heap:
            curDist, curr = heappop(heap)
            if curDist > shortDist[curr]:
                continue
            
            for next, w in graph[curr]:
                distance = curDist + w
                if distance < shortDist[next]:
                    shortDist[next] = distance
                    heappush(heap, (distance, next))   
        
        #kepp only the roads which belong to a shortest path 
        graph, inDegrees = self.pruneRoads(roads, shortDist)
        
        #Get a topological sorted order of the DAG
        topOrder = self.topologicalSort(graph, inDegrees)
        #What remains now is to count the total number of ways to get to n-1 Similiar to 797
        ways = {i:0 for i in graph}
        ways[0] = 1##ONly one way to reach the root node, starting at it
        for u in topOrder:
            for v in graph[u]:
                ways[v] += ways[u]#Every path ending at u can be extended to v
                
                
        return ways[n-1] % (pow(10, 9) + 7)
    
    def topologicalSort(self, graph, inDegrees):
        q = deque()
        for node in graph:
            if inDegrees[node] == 0:
                q.append(node)
        
        order = []                
        while q:
            node = q.popleft()
            order.append(node)
            for next in graph[node]:
                inDegrees[next] -= 1
                if inDegrees[next] == 0:
                    q.append(next)
        return order
# @lc code=end

