#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        the max sum of any subarray
        each tree only have a single fruit
        """
        n = len(fruits)
        window= Counter()
        res = 0
        l = 0
        for r in range(n):
            window[fruits[r]] += 1
            while len(window) > 2:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1
            
            res = max(res, (r - l+1))
        return res

            
            
            
        
# @lc code=end

