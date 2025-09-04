#
# @lc app=leetcode id=3516 lang=python3
#
# [3516] Find Closest Person
#

# @lc code=start
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_dist = abs(x -z)
        y_dist = abs(y-z)
        if x_dist < y_dist:
            return 1
        elif x_dist > y_dist:
            return 2
        else:
            return 0
        
# @lc code=end

