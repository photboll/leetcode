#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """Number of connected components of a graph"""
        n = len(isConnected)
        num_provinces = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            
            num_provinces += 1
            stack = [i]
            visited.add(i)
            while stack:
                cur_city = stack.pop()
                for next_city in range(n):
                    if isConnected[cur_city][next_city] == 1 and next_city not in visited:
                        visited.add(next_city)
                        stack.append(next_city)
        return num_provinces
            
            
         
# @lc code=end

