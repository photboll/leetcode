#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        
        def dp(i, own_share):
            if i == len(prices):
                return 0
            
            if (i, own_share) in memo:
                return memo[(i, own_share)]
            result = 0
            if own_share:
                result = max(
                    dp(i+1, own_share), #Do nothing
                    prices[i] + dp(i+1, False)# sell share
                )
            else:
                result = max(
                    dp(i+1, own_share), #Do nothing
                    -prices[i] - fee + dp(i+1, True)
                )
            
            memo[(i, own_share)] = result
            return result
        return dp(0, False)
            
        
# @lc code=end

