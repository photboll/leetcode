# @lc app=leetcode id=836 slug=rectangle-overlap lang=python3
#
# [836] Rectangle Overlap
# Difficulty: Easy
# Tags: Math, Geometry
# URL: https://leetcode.com/problems/rectangle-overlap/
#
# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or 
            rec2[0] == rec2[2] or rec2[1] == rec2[3]
            ):
            return False
        
        return not(
            rec1[2] <= rec2[0] or # to the left 
            rec1[0] >= rec2[2] or # right
            rec1[3] <= rec2[1]or # bottom
            rec1[1] >= rec2[3] #top
        )

# @lc code=end
