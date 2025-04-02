#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ss = s + s
        n = len(s)
        for i in range(n):
            if ss[i:i+n] == goal:
                return True
            
        return False
# @lc code=end

