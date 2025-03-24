#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {} 
        #iDay is the index of the starting day
        #salesRemaining is how many times we can sell a stock again 
        #ownShare wheter or not we are a shareholder on iDay
        def dp(iDay, salesRemaining, ownShare):
            #We have run out of days or total transaction 
            if iDay == len(prices) or salesRemaining == 0:
                return 0
            if (iDay, salesRemaining, ownShare) in memo:
                return memo[(iDay, salesRemaining, ownShare)]
            result = 0
            
            #We can sell our share if we have one
            if ownShare:
                result = max(#We choose the option which maximizes the return 
                    dp(iDay+1, salesRemaining, ownShare),#Keep holding
                    prices[iDay] + dp(iDay, salesRemaining - 1, False)#Or sell the share
                          )
            else:
                result = max(
                    dp(iDay+1, salesRemaining, ownShare),#Don't buy
                    -prices[iDay] + dp(iDay +1, salesRemaining, True)#Or buy a share today
                )

            memo[(iDay, salesRemaining, ownShare)] = result
            return result
        return dp(0, k, False)       
# @lc code=end

