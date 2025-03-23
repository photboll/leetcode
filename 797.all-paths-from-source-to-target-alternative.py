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
        def dfs(path):
            if path[-1] == n - 1:
                #We ahve reached the target
                result.append(list(path))
                return
            
            for v in graph[path[-1]]:
                dfs(path + [v])
        
        dfs([0])
        return result     
        
# @lc code=end

