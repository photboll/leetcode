#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
         a/ b = n_1 implies that a = n_1 * b 
         we let each variable A_i be a vertex. each equation:value will then be a directed edge from one value to another
         Then the answer of each query will simply be the total product of each in the path from C to D 
        """
        edges = defaultdict(list)
        for (a, b), n in zip(equations, values):
            edges[a].append((b, n))
            edges[b].append((a, 1/n))
        
        def bfs(start, target):
            queue = deque()
            queue.append((start, 1.0))#Node name, total weight 
            visited = set()#Be careful to add the whole word to visited and not its chars 
            visited.add(start)
            while queue:
                curr_node, curr_weight = queue.popleft()
                if curr_node == target:
                    return curr_weight
                for next_node, weight in edges[curr_node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append((next_node, weight * curr_weight))
            #if we never come across the target during bfs
            #Then they must be in different subgraphs, and there the query can't be answered
            return -1.0
        results = []
        for c, d in queries:
            if c not in edges or d not in edges:
                #The queried variables have to at least exist in the graph
                results.append(-1.0)
                continue
            results.append(bfs(c, d))
        return results
        
        
        
# @lc code=end

