#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start
from collections import Counter

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freqs = Counter(costs)
        result = 0

        keys = list(freqs.keys())
        keys.sort()

        for key in keys:
            if key * freqs[key] <= coins:
                result += freqs[key]
                coins -= key * freqs[key]
            else:
                k =  coins // key
                result += k
                coins -= k * key
                break

        return result 
        
# @lc code=end

