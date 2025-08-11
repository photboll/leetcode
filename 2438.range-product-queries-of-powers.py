#
# @lc app=leetcode id=2438 lang=python3
#
# [2438] Range Product Queries of Powers
#

# @lc code=start


MOD = pow(10, 9) + 7
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        the powers array is easily found by looking at the most signigicant bit of n 
        """
        def get_powers_exponents(n):
            powers = []
            x = 1
            exponents = 0
            while n > 0:
                if n & 1:
                    powers.append(exponents)
                x = x << 1
                exponents += 1
                n = n >> 1
            return powers

        exponents = get_powers_exponents(n)
        
        res = []
        for l, r in queries:
            exp = sum(exponents[l:r+1])
            res.append(pow(2, exp, MOD))
        return res
        
# @lc code=end

