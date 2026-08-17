#
# @lc app=leetcode id=3016 lang=python3
#
# [3016] Minimum Number of Pushes to Type Word II
#

# @lc code=start
from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = list(Counter(word).items())
        counts.sort(key= lambda x: -x[1])
        presses_per_key = 1
        available_keys = 8
        total = 0
        for char, cnt in counts:
            if available_keys == 0:
                available_keys = 8
                presses_per_key += 1

            total += presses_per_key * cnt
            available_keys -= 1

        return total 



        
# @lc code=end

