#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
def dfs(node, edges, dist, visited):
    visited[node] = True
    neighbor = edges[node]
    if neighbor != -1 and not visited[neighbor]:
        dist[neighbor] = 1+ dist[node]
        dfs(neighbor, edges, dist, visited)


        
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [float("inf")] * n
        dist2 = [float("inf")] * n
        dist1[node1] = 0
        dist2[node2] = 0
        
        visited1 = [False] * n
        visited2 = [False] * n
        
        dfs(node1, edges, dist1, visited1)
        dfs(node2, edges, dist2, visited2)

        min_dist_node = -1
        min_dist = float("inf")
        for cur_node in range(n):
            cur_dist = max(dist1[cur_node], dist2[cur_node])
            if min_dist > cur_dist:
                min_dist_node = cur_node
                min_dist = cur_dist
        return min_dist_node
        
# @lc code=end

