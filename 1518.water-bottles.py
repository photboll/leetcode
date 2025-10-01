#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        while numBottles >= numExchange:
            #Every numExchnage bootles drunk will give a new full bottle 
            div, rem = divmod(numBottles, numExchange)
            total += numBottles - rem
            numBottles = div + rem
        total += numBottles
        return total 

            
        
# @lc code=end

