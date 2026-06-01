#
# @lc app=leetcode id=2144 lang=python3
#
# [2144] Minimum Cost of Buying Candies With Discount
#

# @lc code=start
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        res = 0

        for i in range(len(cost)):
            if i % 3 != 2:
                res += cost[i]
        return res 


        
# @lc code=end

