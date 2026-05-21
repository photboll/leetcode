#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        Bfs search. conditions in the task defines the valid edges 
        """
        
        n = len(arr)

        if n == 1:
            return 0
        
        mp = defaultdict(list)

        for i in range(n):
            mp[arr[i]].append(i)
        
        q = deque([(0,0)])
        visited = [0] * n 
        visited[0] = 1

        while q:
            node, dist = q.popleft()

            if node == n-1:
                return dist
            
            if node-1 >= 0 and not visited[node-1]:
                visited[node-1] = 1
                q.append((node-1, dist+1))
            
            if node + 1 < n and not visited[node+1]:
                visited[node+1] = 1
                q.append((node+1, dist+1))
            
            for neigh in mp[arr[node]]:
                if not visited[neigh]:
                    visited[neigh] = 1
                    q.append((neigh, dist+1))
            
            mp[arr[node]].clear()

        return -1 



        
        
# @lc code=end

