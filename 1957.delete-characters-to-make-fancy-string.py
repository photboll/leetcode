#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#

# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        prev_char = ""
        count = 0
        for char in s:
            if char == prev_char:
                count += 1
            else:
                res.append(prev_char*min(2, count))
                count = 1
                prev_char = char

        res.append(prev_char*min(2, count))

        return "".join(res)
        
# @lc code=end

