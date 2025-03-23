#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        dayBought = None
        for i in range(len(prices)-1):
            #the price will decrease and we hold a share, sell to make a profit
            if prices[i+1] < prices[i] and dayBought is not None:
                totalProfit += prices[i] - prices[dayBought]
                dayBought = None
            elif prices[i+1] > prices[i] and dayBought is None:
                #The prices will increase and we do not have a share, buy one
                dayBought = i
        
        #are we a share holder at the end, sell it for a final profit
        if dayBought is not None:
            totalProfit += prices[-1] - prices[dayBought]
            

        return max(totalProfit, 0)
        
# @lc code=end

