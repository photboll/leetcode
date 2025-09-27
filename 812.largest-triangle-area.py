#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#

# @lc code=start
from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        How do we compute the area of a triangle defined by three points?
        Area = base * height / 2
        Can we choose the points arbitrarily when converting from base to height?yes
        base is p1 to p2. Is the height then p2 to p3(or p2 to p3)? or do I have to do some more math?
        do i have to compute the dot product then find the angle between them and then do base * sin(angle)
        """
        def triangle_area(p1, p2, p3):
            #Triangle is defined by the three corner points
            #Area computed by shoelace formula
            area = p1[0] * (p2[1] - p3[1])
            area += p2[0] * (p3[1] - p1[1])
            area += p3[0] * (p1[1] - p2[1])
            return abs(area)/ 2
        
        res = 0 
        for (p1, p2, p3) in combinations(points, 3):
            res  = max(res, triangle_area(p1, p2, p3))
        
        return res


        
# @lc code=end

