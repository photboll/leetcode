#
# @lc app=leetcode id=1611 lang=python3
#
# [1611] Minimum One Bit Operations to Make Integers Zero
#

# @lc code=start
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        k = 0
        curr = 1
        while (curr << 1) <= n:
            curr = (curr << 1)
            k += 1
        
        return pow(2, k+1) - 1 -self.minimumOneBitOperations(n^curr)

        
# @lc code=end

