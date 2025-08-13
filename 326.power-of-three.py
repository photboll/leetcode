#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
MAX_N = (1 << 31) -1 
x = 1 
while 3*x < MAX_N:
    x *= 3
    
MAX_3_POWER = x
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #print(MAX_3_POWER)
        if n < 1:
            return False
        return MAX_3_POWER % n == 0

        
# @lc code=end

