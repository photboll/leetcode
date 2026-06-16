#
# @lc app=leetcode id=3612 lang=python3
#
# [3612] Process String with Special Operations I
#

# @lc code=start
class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for char in s:
            if char == "*":
                try:
                    result.pop()
                except IndexError:
                    pass
            elif char == "#":
                result.extend(result)
            elif char == "%":
                result.reverse()
            elif char.islower():
                result.append(char)
            
        
        return "".join(result)
        
# @lc code=end

