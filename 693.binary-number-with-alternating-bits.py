#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        tmp = (n >> 1) + n
        return (tmp & tmp + 1) == 0
    
    
    

        
# @lc code=end

