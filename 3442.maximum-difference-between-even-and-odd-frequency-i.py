#
# @lc app=leetcode id=3442 lang=python3
#
# [3442] Maximum Difference Between Even and Odd Frequency I
#

# @lc code=start
from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = Counter(s)

        max_odd = 0
        min_even = float("inf")
        
        for k in freqs:
            if freqs[k] % 2 == 0:
                min_even = min(min_even, freqs[k])
            else:
                max_odd = max(max_odd, freqs[k])
        return max_odd - min_even
        
# @lc code=end

