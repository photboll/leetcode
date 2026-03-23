#
# @lc app=leetcode id=1886 lang=python3
#
# [1886] Determine Whether Matrix Can Be Obtained By Rotation
#

# @lc code=start
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(row) for row in zip(*mat[::-1])]
        return False
        
# @lc code=end

