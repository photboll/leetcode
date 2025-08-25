#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        for d in range(m + n - 1):
            intermediate = []
            
            # Starting row and column for this diagonal
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            
            # Collect all elements along this diagonal
            while r < m and c >= 0:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            # Reverse on even diagonals
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        
        return result

        
# @lc code=end

