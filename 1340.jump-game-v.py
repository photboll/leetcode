#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#

# @lc code=start
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        visited = {}

        def dfs(pos):
            if pos in visited:
                return 

            visited[pos] = 1

            i = pos -1
            while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
                dfs(i)
                visited[pos] = max(visited[pos], visited[i] + 1)
                i -= 1
            
            i = pos + 1
            while i < len(arr) and i - pos <= d and arr[pos] > arr[i]:
                dfs(i)
                visited[pos] = max(visited[pos], visited[i] + 1)
                i += 1
        
        for i in range(len(arr)):
            dfs(i)
        return max(visited.values())


        
# @lc code=end

