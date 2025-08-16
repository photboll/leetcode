#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = str(num)
        for i in range(len(digits)):
            if digits[i] == "6":
                return int(digits[:i] + "9" + digits[i+1:])
        
        return num
        
        
# @lc code=end

