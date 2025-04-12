#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Topological sort the course prerequisites
        in_degrees = [0] * numCourses
        edges = defaultdict(list)
        for a, b in prerequisites:
            in_degrees[a] += 1
            edges[b].append(a)
        stack = []
        for node in range(numCourses):
            if in_degrees[node] == 0:
                #A course without prerequisites can always be taken 
                stack.append(node)
            
        ordered = []
        while stack:
            curr_node = stack.pop()
            ordered.append(curr_node)
            for next_node in edges[curr_node]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    stack.append(next_node)
        #print(ordered)
        #every remaining node needs to have an indegree of 0 after the sorting
        return max(in_degrees) == 0
            
# @lc code=end

