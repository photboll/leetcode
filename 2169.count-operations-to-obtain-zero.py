#
# @lc app=leetcode id=2169 lang=python3
#
# [2169] Count Operations to Obtain Zero
#

# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0

        while num1 > 0 and num2 > 0:
            ops += 1
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
        
        
        return ops
        
# @lc code=end

