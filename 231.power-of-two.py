#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n -1)) == 0
class SolutionV1:
    def isPowerOfTwo(self, n: int) -> bool:

        for i in range(32):
            num = (1 << i)
            if num == n:
                return True
            elif num > n:
                break 
        
        return False
        
# @lc code=end

