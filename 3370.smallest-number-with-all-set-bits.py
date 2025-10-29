#
# @lc app=leetcode id=3370 lang=python3
#
# [3370] Smallest Number With All Set Bits
#

# @lc code=start
class Solution:
    def smallestNumber(self, n: int) -> int:
        result = 0
        while n > 0:
            n = n >> 1
            result = (result << 1)| 1
            #print(f"{result:b}")
        return result
            
    
        
# @lc code=end

