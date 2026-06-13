#
# @lc app=leetcode id=3838 lang=python3
#
# [3838] Weighted Word Mapping
#

# @lc code=start
from string import ascii_lowercase
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        w2c = { i:c for i,c in enumerate(ascii_lowercase[::-1])}
        weight_dict = {chr(i + 97):w for i, w in enumerate(weights) }
        result = []

        for word in words:
            total = 0
            for c in word:
                total = (total + weight_dict[c]) % 26
            result.append(w2c[total])
        return "".join(result)
        
# @lc code=end

