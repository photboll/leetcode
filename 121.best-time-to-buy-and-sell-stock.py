#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        lowestPrice = prices[0]
        for price in prices:
            lowestPrice = min(lowestPrice, price)
            bestProfit = max(bestProfit, price - lowestPrice)
        return bestProfit
        
               
# @lc code=end

