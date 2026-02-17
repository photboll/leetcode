#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        #print(bin(n))
        for _ in range(31):
            res |= (n & 1)
            res <<= 1
            n >>= 1

        #print(bin(res))
        return res
        
# @lc code=end

