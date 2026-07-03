#
# @lc app=leetcode id=3620 lang=python3
#
# [3620] Network Recovery Pathways
#

# @lc code=start
from collections import defaultdict, deque
from heapq import heappop, heappush

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        """
        is there any point in haveing the offline nodes in the graph at all?
        i dont think there is. i should be able to prune them ahead of time
        though it is premature optimization. 
        what is meant with recovery cost? what does recovery even mean here. probably something about network nodes
        """
        n = len(online)
        u2v = defaultdict(list)
        costs = set()

        for u, v, c in edges:
            if online[u] and online[v]:
                u2v[u].append((v, c))
                costs.add(c)

        def check(min_cost):
            pq  = [(0, 0)]
            visited = set()

            while pq:
                cur_cost, curr = heappop(pq)
                if curr in visited:
                    continue

                visited.add(curr)

                if cur_cost > k:
                    return False

                if curr == n-1:
                    return True

                for neigh, cost in u2v[curr]:
                    if cost >= min_cost:
                        if neigh not in visited:
                            heappush(pq, (cur_cost + cost, neigh))
            return False
        
        
        sorted_costs = sorted(costs)
        lo, hi = 0, len(sorted_costs) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(sorted_costs[mid]):
                ans = sorted_costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
        
        



        


        
# @lc code=end

