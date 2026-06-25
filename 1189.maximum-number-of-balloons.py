#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target_cnt = Counter("balloon")
        freqs = Counter(text)
        result = float("inf")

        for char in target_cnt.keys():
            if freqs[char] == 0:
                return 0 

            result = min(result, 
                         freqs[char] // target_cnt[char]
                         )
        return result




        
# @lc code=end

