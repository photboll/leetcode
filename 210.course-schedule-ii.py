#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0] * numCourses
        edges = defaultdict(list) 
        for u, v in prerequisites:
            in_degrees[u] += 1
            edges[v].append(u)
        
        stack = []
        for node in range(numCourses):
            if in_degrees[node] == 0:
                stack.append(node)
        
        ordered = []
        while stack:
            curr_node = stack.pop()
            ordered.append(curr_node)
            for next_node in edges[curr_node]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    stack.append(next_node)
        return ordered if len(ordered) == numCourses else []
# @lc code=end

