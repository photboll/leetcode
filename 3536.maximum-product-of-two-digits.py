#
# @lc app=leetcode id=3536 lang=python3
#
# [3536] Maximum Product of Two Digits
#

# @lc code=start
class Solution:
    def maxProduct(self, n: int) -> int:
        mx1 = 0
        mx2 = 0
        
        while n > 0:
            n, digit = divmod(n, 10)
            if digit > mx1:
                mx2 = mx1 
                mx1 = digit
            elif digit > mx2:
                mx2 = digit
        return mx1 * mx2
        
            
        
# @lc code=end

