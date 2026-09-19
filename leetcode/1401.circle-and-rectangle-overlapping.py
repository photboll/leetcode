# @lc app=leetcode id=1401 slug=circle-and-rectangle-overlapping lang=python3
#
# [1401] Circle and Rectangle Overlapping
# Difficulty: Medium
# Tags: Math, Geometry
# URL: https://leetcode.com/problems/circle-and-rectangle-overlapping/
#
# @lc code=start
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def euclidean_distance2(a1, b1, a2, b2):
            return (a2 - a1)**2 + (b1 - b2)**2
        #Chech if the circle is inside the rectangle
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True

        candidates = [
            (max(x1, min(xCenter, x2)), y1), # Bottom line segment to the center
            (max(x1, min(xCenter, x2)), y2), # Top line segment to the center
            (x1, max(y1, min(yCenter, y2))), # left line segment to the center
            (x2, max(y1, min(yCenter, y2))), # right line segment to the center
        ]

        
        for cand in candidates:
            dist = euclidean_distance2(xCenter, yCenter, *cand)
            if dist <= radius**2:
                return True
        
        return False 
        

# @lc code=end
