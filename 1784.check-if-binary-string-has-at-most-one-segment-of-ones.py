#
# @lc app=leetcode id=1784 lang=python3
#
# [1784] Check if Binary String Has at Most One Segment of Ones
#

# @lc code=start
class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        i0 = s.find("0")
        if i0 == -1:
            return True
        i1 = s.rfind("1")
        return i0 > i1
        
# @lc code=end

