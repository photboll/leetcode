#
# @lc app=leetcode id=1925 lang=python3
#
# [1925] Count Square Sum Triples
#

# @lc code=start
from math import sqrt
class Solution:
    def countTriples(self, n: int) -> int:
        squares = {c * c for c in range(1, n+1)}
        res = 0
        
        for a in range(1, n+1):
            for b in range(1, n+1):
                if (a**2 + b**2 ) in squares:
                    res += 1
        return res 
                
        
# @lc code=end

