#
# @lc app=leetcode id=1680 lang=python3
#
# [1680] Concatenation of Consecutive Binary Numbers
#

# @lc code=start
MOD = pow(10, 9) + 7

class Solution:
    def concatenatedBinary(self, n: int) -> int:

        length = 0
        result = 0
        for i in range(1, n+1):
            if i.bit_count() == 1:
                length += 1
            result = ((result << length) % MOD + i) % MOD
        return result

# @lc code=end

