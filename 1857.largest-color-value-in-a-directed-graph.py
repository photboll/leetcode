#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        in_degree = [0] * n
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
            
            
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        dp = [[0] * 26 for _ in range(n)]
        
        max_path_color_value = 0
        processed_nodes_count = 0
        
        while queue:
            u = queue.popleft()
            processed_nodes_count += 1
            
            color_u_idx = ord(colors[u]) - ord("a")
            dp[u][color_u_idx] += 1
            
            max_path_color_value = max(max_path_color_value, dp[u][color_u_idx])

            for v in adj[u]:
                
                for c_idx in range(26):
                    dp[v][c_idx] = max(dp[v][c_idx], dp[u][c_idx])
                
                in_degree[v] -= 1
                
                if in_degree[v] == 0:
                    queue.append(v)
        
        if processed_nodes_count < n:
            return -1
        else:
            return max_path_color_value
            
            
# @lc code=end

