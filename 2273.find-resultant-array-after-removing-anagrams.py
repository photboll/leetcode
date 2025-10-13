#
# @lc app=leetcode id=2273 lang=python3
#
# [2273] Find Resultant Array After Removing Anagrams
#

# @lc code=start
from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        freqs = [Counter(word) for word in words]
        result = [words[0]]
        for i in range(1, n):
            if freqs[i] != freqs[i-1]:
                result.append(words[i])

        return result
        
# @lc code=end

