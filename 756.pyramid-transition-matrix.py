#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#

# @lc code=start
from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        transitions = defaultdict(set)
        for u, v, w in allowed:
            transitions[u, v].add(w)
        
        def add_neighbor(node):
            #build all possible next rows for the current node(row)
            res = ['']
            for i in range(1, len(node)):
                eles = transitions[(node[i-1], node[i])]      

                if eles:
                    res = [a + e for e in eles for a in res]
                else:
                    return []
            return res
        
        visited = set()

        def dfs(node):
            #A node is a single row in the pyramid
            if len(node) ==1:
                return True
            if node in visited:
                return False
            
            for next in add_neighbor(node):
                if dfs(next):
                    return True

            visited.add(node)
            return False

        return dfs(bottom)

        
# @lc code=end

