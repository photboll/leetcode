#
# @lc app=leetcode id=3541 lang=python3
#
# [3541] Find Most Frequent Vowel and Consonant
#

# @lc code=start
from collections import Counter
VOWELS = set(c for c in "aeiou")
class Solution:
    def maxFreqSum(self, s: str) -> int:

        cons_freqs = Counter()
        cons_freqs["s"] = 0
        vow_freqs = Counter()
        vow_freqs["a"] = 0
        for c in s:
            if c in VOWELS:
                vow_freqs[c] += 1
            else:
                cons_freqs[c] += 1

        #print(vow_freqs, cons_freqs)
        return max(vow_freqs.values()) + max(cons_freqs.values())
                

        
# @lc code=end

