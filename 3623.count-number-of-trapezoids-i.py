#
# @lc app=leetcode id=3623 lang=python3
#
# [3623] Count Number of Trapezoids I
#

# @lc code=start
MOD = pow(10, 9) + 7
from collections import Counter
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        Two points make a line.
        Any two horizontal lines can be used to make a trapezoid
        a horizontal line is made by any two points which share a y-coord

        Find all horizontal lines. important they can not be coolinear 
        """
        freqs = Counter(p[1] for p in points)

        c2 = 0
        s = 0
        for f in freqs.values():
            if f <= 1:#a single point can not make a line
                continue
            c = f *(f-1) //2
            s += c
            c2 += c*c
                
                
        return (s*s - c2) // 2 % MOD
        
# @lc code=end

