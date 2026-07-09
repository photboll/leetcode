#
# @lc app=leetcode id=3754 lang=python3
#
# [3754] Concatenate Non-Zero Digits and Multiply by Sum I
#

# @lc code=start
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = "".join(["" if c == "0" else c for c in str(n)])
        #print(x)
        if x == "":
            return 0
        x = int(x)
        #print(x)

        def digit_sum(num):
            s = 0
            while num > 0:
                num, rem = divmod(num, 10)
                s += rem
            return s
        
        return x * digit_sum(x)
        
# @lc code=end

