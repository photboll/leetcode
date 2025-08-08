#
# @lc app=leetcode id=808 lang=python3
#
# [808] Soup Servings
#

# @lc code=start
from functools import cache
OPS = [(-100, 0), (-75, -25), (-50, -50), (-25, -75)]


class Solution:
    def soupServings(self, n: int) -> float:
        A = B = n
        probA = 0
        prev_prob = 0
        
        while abs(probA - prev_prob) > 1e6:
            prev_prob = probA
            
            if A<= 0 and B <= 0:
                break 
            pass
class SolutionRecur:
    def soupServings(self, n: int) -> float:
        """
        The starting volume of both bowls are always the same
        This one uses a hard coded cust off. 
        We can instead create an exit condition if we had done a bottom up iterative approach instead
        """
        
        @cache
        def dp(A, B):
            if A <= 0 and B <= 0:#Both bowls become empty at the same time 
                return 0.5
            elif A <= 0:
                return 1.0
            elif B <= 0:
                return 0.0
            
            #Both bowls have soup remaining 
            prob = 0.0
            for dA, dB in OPS:
                prob += dp(A+dA, B+dB)
            
            prob *= 1 / len(OPS)

            return prob
            
        if n > 5000:
            return 1.0
        else:
            return dp(n, n)
        
# @lc code=end

