#
# @lc app=leetcode id=3345 lang=python3
#
# [3345] Smallest Divisible Digit Product I
#

# @lc code=start
MAX_N = 101
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            res = 1
            while num > 0:
                num, digit = divmod(num, 10)
                res *= digit
            return res
                

        for num in range(n, MAX_N):
            if digit_product(num) % t == 0:
                return num
        

        
# @lc code=end

