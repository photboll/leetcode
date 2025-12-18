#
# @lc app=leetcode id=3652 lang=python3
#
# [3652] Best Time to Buy and Sell Stock using Strategy
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        total = 0
        max_s = 0
        s = 0
        for i, (p, st) in enumerate(zip(prices, strategy)):
            total += p * st

            s += p *(1 - st)

            if i < k-1:
                if i >= k // 2 - 1:
                    s -= prices[i - k//2 + 1]
                continue
            
            max_s = max(max_s, s)

            s -= prices[i- k//2 + 1] - prices[i -k + 1] * strategy[i-k+1]

        return total + max_s 

        
# @lc code=end

