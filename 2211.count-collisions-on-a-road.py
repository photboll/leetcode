#
# @lc app=leetcode id=2211 lang=python3
#
# [2211] Count Collisions on a Road
#

# @lc code=start
class Solution:
    def countCollisions(self, directions: str) -> int:
        #the first cars going to the left are always safe
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")
        return directions.count("R") + directions.count("L")
        
# @lc code=end

