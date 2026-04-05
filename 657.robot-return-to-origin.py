#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        x = 0
        y = 0
        for m in moves:
            if m == "R":
                x += 1
            elif m == "L":
                x -= 1
            elif m == "U":
                y += 1
            else:#Down
                y -= 1
        return x == 0 and y == 0
        
# @lc code=end

