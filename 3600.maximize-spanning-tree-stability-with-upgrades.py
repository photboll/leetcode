#
# @lc app=leetcode id=3600 lang=python3
#
# [3600] Maximize Spanning Tree Stability with Upgrades
#

# @lc code=start

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] *n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True



class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def feasible(min_strength):
            uf = UnionFind(n)
            edges_used = 0
            upgrades_used = 0

            for u, v, s, must in edges:
                if must == 1:
                    if s < min_strength:
                        return False# must edge to weak, impossible to meet target
                    if not uf.union(u, v):
                        return False #Must edge create a cycle
                    edges_used += 1

            #optional edges that do no need to be upgraded (x >= min_strenght)
            no_upgrade = [(u, v, s) for u,v,s, must in edges if must == 0 and s>=min_strength]
            #
            need_upgrade = [(u, v, s) for u, v,s, must in edges if must == 0 and s < min_strength and 2 * s >= min_strength]
    
                    # Sort by strength descending (greedy: pick strongest first)
            no_upgrade.sort(key=lambda x: -x[2])
            need_upgrade.sort(key=lambda x: -x[2])
            
            for u, v, s in no_upgrade:
                if uf.union(u, v):
                    edges_used += 1
            
            for u, v, s in need_upgrade:
                if uf.union(u, v):
                    if upgrades_used < k:
                        upgrades_used += 1
                        edges_used += 1
                    else:
                        return False  # Need upgrade but no budget left
            
            return edges_used == n - 1
        
        # Check if any spanning tree is possible at all
        if not feasible(0):
            return -1
        
        max_s = max(s for _, _, s, _ in edges)
        lo, hi = 1, 2 * max_s
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
# @lc code=end

