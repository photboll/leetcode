#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dp(day_i, own_share, can_buy) -> int:
            if day_i == len(prices):
                return 0
            if (day_i, own_share, can_buy) in memo:
                return memo[(day_i, own_share, can_buy)]
            result = 0
            #If we own a share we can either pass or sell on this day
            if own_share:
                result =  max(
                    dp(day_i + 1, own_share, True), #Pass 
                    prices[day_i] + dp(day_i +1, False, False)#Sell 
                )
            elif can_buy:
                result =  max(
                 dp(day_i +1, False, True), #Pass
                 -prices[day_i] + dp(day_i +1, True, False)#Buy
                )
            else:
                #if we don#t have a share and are not allowed to buy one we have to pass this day
                result = dp(day_i +1, False, True)
                
            memo[(day_i, own_share, can_buy)] = result
            return result
        
        dp(0, False, True)
        #print(memo)
        return memo[(0, False, True)]
        
# @lc code=end

