#
# @lc app=leetcode id=3418 lang=python3
#
# [3418] Maximum Amount of Money Robot Can Earn
#

# @lc code=start
from functools import cache
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        """
        dp 
        keep track of current maximum and number of neutralizations left at each step
        """

        m = len(coins)
        n = len(coins[0])

        @cache
        def dp(r, c, neutralizations_remaining):
            if r == 0 and c == 0 and neutralizations_remaining == 0:
                return coins[r][c]
            elif r == 0 and c == 0:
                #if we hav neutralizations left we can stop the robber if it exists
                return max(coins[r][c], 0)

            up = dp(r-1, c, neutralizations_remaining) if r > 0 else float("-inf")
            left = dp(r, c-1, neutralizations_remaining) if c > 0 else float("-inf")

            # Option 1 accept the coin value. regardless if positive or negative
            res = coins[r][c] + max(up, left)

            # Option 2 neutralize currently negative cell
            if coins[r][c] < 0 and neutralizations_remaining > 0:
                res = max(
                    res, 
                    dp(r-1, c, neutralizations_remaining-1) if r > 0 else float("-inf"),
                    dp(r, c-1, neutralizations_remaining-1) if c > 0 else float("-inf")
                )
            return res

        result = dp(m-1, n-1, 2)
        dp.cache_clear()
        return result
            






        
        
        
        
# @lc code=end

