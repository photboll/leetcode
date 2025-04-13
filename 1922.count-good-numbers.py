#
# @lc app=leetcode id=1922 lang=python3
#
# [1922] Count Good Numbers
#

# @lc code=start
from functools import cache
MOD = pow(10, 9) + 7
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #eihter we are at an even position in which case we can choose one of [0, 2, 4, 6, 8]
        #or we are at an odd position in which case we can choose one of [2, 3, 5, 7]
        #Leading zeros are allowed so
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD
# @lc code=end

