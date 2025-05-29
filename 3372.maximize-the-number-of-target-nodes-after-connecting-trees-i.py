#
# @lc app=leetcode id=3372 lang=python3
#
# [3372] Maximize the Number of Target Nodes After Connecting Trees I
#

# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(node, parent, children, k) -> int:
            if k < 0:
                return 0
            res = 1
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, children, k-1)
            return res

        def build(edges, k):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            
            res = [0] * n
            for i in range(n):
                res[i] = dfs(i, -1, children, k)
            return res


        n = len(edges1) + 1
        count1 = build(edges1, k)
        count2 = build(edges2, k-1)
        maxCount2 = max(count2)
        res = [count1[i]+ maxCount2 for i in range(n)]
        return res
    
        
        
# @lc code=end

