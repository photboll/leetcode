#
# @lc app=leetcode id=3161 lang=python3
#
# [3161] Block Placement Queries
#

# @lc code=start
class Node:
    def __init__(self):
        self.value = 0
        self.L = None
        self.R = None
    
class DynamicSegmentTree:
    def __init__(self, lo:int, hi:int):
        self.lo = lo
        self.hi = hi
        self.pool = [Node()]
        self.root = 0

    def _new_node(self) -> int:
        self.pool.append(Node())
        return len(self.pool) -1
        
    
    def update(self, pos:int, val:int, node:int=None, l:int=None, r:int=None) ->:
        if node is None:
            node, l, r = self.root, self.lo, self.hi
            self.root = self._update(node, l, r, pos, val)
            return self.root
        return self._update(node, l, r, pos, val)
    
    def _update(self, node:int, l:int, r:int, pos:int, val:int) -> int:
        if not node:
            node = self._new_node()
        p = self.pool[node]
        
        if l == r:
            

        
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
# @lc code=end

