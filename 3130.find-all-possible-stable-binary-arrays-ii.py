#
# @lc app=leetcode id=3130 lang=python3
#
# [3130] Find All Possible Stable Binary Arrays II
#

# @lc code=start
from functools import cache
MOD = pow(10, 9) + 7

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        @cache
        def dp(zero, one, last_bit):
            if zero == 0:
                return 1 if last_bit == 1 and one <= limit else 0
            elif one == 0:
                return 1 if last_bit == 0 and zero <= limit else 0
            
            if last_bit == 0:
                res = dp(zero -1, one, 0) + dp(zero-1, one, 1)
                if zero > limit:
                    res -= dp(zero-limit-1, one, 1)
            else:
                res = dp(zero, one-1, 0) + dp(zero, one-1, 1)
                if one > limit:
                    res -= dp(zero, one - limit -1, 0)
            return res % MOD
        res = (dp(zero, one, 0) + dp(zero, one, 1)) % MOD
        dp.cache_clear()
        return res
        
# @lc code=end

