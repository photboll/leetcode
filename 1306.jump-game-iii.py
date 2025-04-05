#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        def recur(i) -> bool :
            if arr[i] == 0:
                return True
            
            visited[i] = True
            left_i = i - arr[i]
            if left_i >= 0 and not visited[left_i]:
                if recur( left_i):
                    return True
                
            
            right_i = i + arr[i]
            
            if right_i < n and not visited[right_i]:
                if recur(right_i):
                    return True
           
            
            return False
        
        return recur(start)
                
        
# @lc code=end

