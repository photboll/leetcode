#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        
        def chebyshev_distance(x1, y1, x2, y2):
            return max(abs(x1 - x2), abs(y1 - y2))
        
        for i in range(1, len(points)):
            result += chebyshev_distance(*points[i-1], *points[i])
        
        return result
            
        
# @lc code=end

