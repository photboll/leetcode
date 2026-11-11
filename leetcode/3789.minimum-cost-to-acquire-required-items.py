# @lc app=leetcode id=3789 slug=minimum-cost-to-acquire-required-items lang=python3
#
# [3789] Minimum Cost to Acquire Required Items
# Difficulty: Medium
# Tags: Math, Greedy
# URL: https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
#
# @lc code=start
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        """
        dp ?
        no greedy should be enough 
        
        if costBoth <= cost1 + cost2 : use those to fill up min(need1, need2)
        the remaining quantity use costBoth or just cost1 or cost2 for the remainder
        """
        result = 0

            
        if costBoth <= cost1 + cost2:
            k = min(need1, need2)
            result += costBoth * k
            need1 -= k
            need2 -= k
        
        if need1 > 0:
            result += min(costBoth, cost1) * need1
        
        if need2 > 0:
            result += min(costBoth, cost2) * need2

        return result
        
        

            
            

        
        
        

# @lc code=end
