#
# @lc app=leetcode id=2785 lang=python3
#
# [2785] Sort Vowels in a String
#

# @lc code=start
VOWELS = set(c for c in "aeiou")
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        vowel_indices = []
        chars = []
        
        for i, c in enumerate(s):
            chars.append(c)
            if c.lower() in VOWELS:
                vowels.append(c)
                vowel_indices.append(i)
        
        vowels.sort()

        for i, c in zip(vowel_indices, vowels):
            chars[i] = c
        
        return "".join(chars)

                
        
# @lc code=end

