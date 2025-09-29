#
# @lc app=leetcode id=1039 lang=python3
#
# [1039] Minimum Score Triangulation of Polygon
#

# @lc code=start
from functools import cache
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i, j):
             if i + 2 > j:
                 return 0
             if i +2 == j:
                 return values[i] * values[i+1] * values[j]
             
             
             return min(
                 (values[i] * values[k] * values[j] + dp(i,k)+dp(k,j)) for k in range(i+1, j)
             )
            
        return dp(0, len(values) -1)
             
        
# @lc code=end

