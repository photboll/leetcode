#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
    
        points.sort(key=lambda x: x[1])
        arrows = 1
        prev_end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= prev_end and points[i][1] >= prev_end:
                continue
            else:
                arrows += 1
                prev_end = points[i][1]
                
        return arrows
    
# @lc code=end

