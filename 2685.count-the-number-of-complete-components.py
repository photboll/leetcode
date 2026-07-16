#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

# @lc code=start
from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        start dfs from each node
        during dfs. 
        count the number of edges on the first node
        all following nodes we visit must have the same number of edges
        and it hace to be m-1 of them
        """

        visited = [False] * n
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        result = 0
        for i in range(n):
            if visited[i]:
                #this nodes belongs to a already processed component
                continue
            
            visited[i] = True
            component = []
            stack = [i]

            while stack:
                curr = stack.pop()
                component.append(curr)

                for neigh in graph[curr]:
                    if not visited[neigh]:
                        visited[neigh] = True
                        stack.append(neigh)
            
            num_nodes = len(component)
            is_complete = True
            for node in component:
                if len(graph[node]) != num_nodes -1:
                    is_complete = False
                    break

            result += is_complete
        return result

            
            
        
        
# @lc code=end

