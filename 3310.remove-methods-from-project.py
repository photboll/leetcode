#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        """
        is this not a problem of removing the connected componoent of k?
        not exactly. i need to considered the directed edges 
        methods that k invokes 
        we add the opposite edges. meaning if a invokes b. we add a to bs list of neighbors

        not enough. need to make sure that no other methods invoke any of the visited ones
        """
        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        visited = [False] * n
        stack = [k]

        while stack:
            curr = stack.pop()
            if visited[curr]:
                continue
            visited[curr] = True

            for neigh in graph[curr]:
                if not visited[neigh]:
                    stack.append(neigh)
        
        # Safety check. does any non-suspicious method invokee a suspicious one
        for u, v in invocations:
            if visited[v] and not visited[u]:
                return list(range(n))

        return [i for i in range(n) if not visited[i]]
        
                

                
            


        
        
# @lc code=end

