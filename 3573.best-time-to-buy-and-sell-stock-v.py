#
# @lc app=leetcode id=3573 lang=python3
#
# [3573] Best Time to Buy and Sell Stock V
#

# @lc code=start
from functools import cache

NEUTRAL, LONG, SHORT = 0, 1, 2

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dp(i, k_remaining, position):
            if i >= n:
                return 0 if position == NEUTRAL else float("-inf")
            if k_remaining == 0:
                return 0 if position == NEUTRAL else float("-inf")
            

            #We can either 1. open long, 2. open short,3. skip. 4.close the current position 
            #Skip, Do nothing 
            result = dp(i+1, k_remaining, position)

            if position == LONG:
                close_long = prices[i] + dp(i+1, k_remaining-1, NEUTRAL)
                result = max(close_long, result)
            elif position == SHORT:
                close_short = -prices[i] + dp(i+1, k_remaining-1, NEUTRAL)
                result = max(close_short, result)
            else:
                open_long = -prices[i] + dp(i+1, k_remaining, LONG)
                open_short = prices[i] + dp(i+1, k_remaining, SHORT)
                result = max(result, open_long, open_short)

            return result 
            
            

        res =  dp(0, k, NEUTRAL)

        dp.cache_clear()
        return res
                
                
            
        
# @lc code=end

