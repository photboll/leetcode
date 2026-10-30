# @lc app=leetcode id=3970 slug=shortest-path-with-at-most-k-consecutive-identical-characters lang=python3
#
# [3970] Shortest Path With At Most K Consecutive Identical Characters
# Difficulty: Medium
# Tags: String, Graph Theory, Heap (Priority Queue), Shortest Path
# URL: https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/
#
# @lc code=start
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        """
        dijkstra and we keep the count of all labels at each state.no not count it is identical 
        
        stats is  total_weight label_count, label, node 
        no , we dont need label just do labels[node]

        """
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        #(node, consecutive_count): 0
        dist = {(0, 1): 0}

        #total_cost, label_count, node
        pq = [(0, 1, 0)]

        while pq:
            cost, label_count, curr = heappop(pq)
            if cost > dist.get((curr, label_count), float("inf")):
                continue

            if curr == n-1:
                return cost

            for neigh, weight in graph[curr]:
                new_count = label_count + 1 if labels[curr] == labels[neigh] else 1
                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist.get((neigh, new_count), float("inf")):
                    dist[(neigh, new_count)] = new_cost
                    heappush(pq, (new_cost, new_count, neigh))
        
        return -1
        
        
                
                


        
        

# @lc code=end
