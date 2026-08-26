#
# @lc app=leetcode id=3622 lang=python3
#
# [3622] Check Divisibility by Digit Sum and Product
#

# @lc code=start
class Solution:
    def checkDivisibility(self, n: int) -> bool:

        def digit_sum(x):
            res = 0
            while x > 0:
                x, digit = divmod(x, 10)
                res += digit
            return res

        def digit_prod(x):
            res = 1
            while x > 0:
                x, digit = divmod(x, 10)
                res *= digit
            return res

        return (n % (digit_prod(n) + digit_sum(n))) == 0
        
# @lc code=end

