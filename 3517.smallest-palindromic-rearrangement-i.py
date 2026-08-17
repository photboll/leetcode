#
# @lc app=leetcode id=3517 lang=python3
#
# [3517] Smallest Palindromic Rearrangement I
#

# @lc code=start
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freqs = Counter([c for c in s])
        prefix = []
        middle = ""
        suffix = []

        for c in "abcdefghijklmnopqrstuvwxyz":
            reps = freqs[c] // 2
            prefix.append(c*reps)
            suffix.append(c*reps)
            if freqs[c] % 2 == 1 and middle == "":
                #can this char be the middle element as well?
                #since we check in order the first candidate will be the optimal 
                #
                middle = c
        
        return "".join(prefix) + middle + "".join(suffix[::-1])
                
            
            
        
# @lc code=end

