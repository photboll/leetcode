#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        result = []
        
        queue = deque([[0]])#Stores the enitre path
        while queue:
            path = queue.popleft()
            u = path[-1]
            if u == n-1:
                result.append(path)
            else:
                for v in graph[u]:
                    queue.append(path + [v])
                        
        
        return result
        
# @lc code=end

