#
# @lc app=leetcode id=3697 lang=python3
#
# [3697] Compute Decimal Representation
#

# @lc code=start
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        i = 1
        while n >  0:
            n, rem = divmod(n, 10)
            if rem > 0:
                res.append(rem * i)
            i *= 10

        
        return res[::-1]
        
# @lc code=end

