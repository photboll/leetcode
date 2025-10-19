#
# @lc app=leetcode id=1625 lang=python3
#
# [1625] Lexicographically Smallest String After Applying Operations
#

# @lc code=start
from collections import deque
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set([s])
        min_s = s
        q = deque([s])
        while q:
            cur = q.popleft()

            if cur < min_s:
                min_s = cur
            
            chars = list(cur)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i])+a) % 10)
            
            neighbor = "".join(chars)
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
            
            rotated = cur[-b:] + cur[:-b]
            if rotated not in visited:
                visited.add(rotated)
                q.append(rotated)
        return min_s
            
            


        
# @lc code=end

