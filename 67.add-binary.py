#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #let a always be the longer string
        if len(a) < len(b):
            a , b = b, a

        def add_digit(d1, d2, carry):
            d3 = d1 + d2 + carry
            return divmod(d3, 2)

        carry = 0
        res = []

        for i in range(1, len(a)+1):
            d1 = int(a[-i])
            d2 = int(b[-i]) if i <= len(b) else 0
            carry, d3 = add_digit(d1, d2, carry)
            res.append(str(d3))
        
        if carry:
            res.append("1")
        return "".join(res[::-1])
            
            

            
            
        
        
        
# @lc code=end

