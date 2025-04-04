#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        is_negative = n < 0
        if is_negative:
            x = 1 / x
            n = -n
        
        tot = 1
        while n > 0:
            if (n & 1):
                tot *= x
            
            x *=  x
            n = (n >> 1)
        return tot
                
            
        
# @lc code=end

