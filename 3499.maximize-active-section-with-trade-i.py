#
# @lc app=leetcode id=3499 lang=python3
#
# [3499] Maximize Active Section with Trade I
#

# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        max_gain = 0

        # runs at even indices are '1'-runs; interior ones are indices 2, 4, ..., len(runs)-3
        for idx in range(2, len(runs) - 1, 2):
            gain = runs[idx - 1][1] + runs[idx + 1][1]  # left zero-run + right zero-run
            max_gain = max(max_gain, gain)

        return s.count('1') + max_gain
        
# @lc code=end

