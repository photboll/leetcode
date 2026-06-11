#
# @lc app=leetcode id=3558 lang=python3
#
# [3558] Number of Ways to Assign Edge Weights I
#

# @lc code=start

from collections import defaultdict
MOD = pow(10, 9) + 7

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        u2v = defaultdict(list)
        for u, v in edges:
            u2v[u].append(v)
            u2v[v].append(u)
        
        visted = set([1])
        stack = [(1, 0)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            for  v in u2v[node]:
                if v not in visted:
                    visted.add(v)
                    stack.append((v, depth+1))
        
        return (1 << (max_depth-1)) % MOD
        

            
        
# @lc code=end

