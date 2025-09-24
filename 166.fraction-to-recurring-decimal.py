#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        
        div, rem = divmod(numerator, denominator)

        res.append(str(div))

        if rem == 0:
            return "".join(res)

        res.append(".")
        
        remainder_map = {}
        while rem != 0:
            if rem in remainder_map:
                res.insert(remainder_map[rem], "(")
                res.append(")")
                break
            remainder_map[rem] = len(res)

            rem *= 10
            div, rem = divmod(rem, denominator)
            res.append(str(div))
        return "".join(res)
        
# @lc code=end

