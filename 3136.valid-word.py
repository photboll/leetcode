#
# @lc app=leetcode id=3136 lang=python3
#
# [3136] Valid Word
#

# @lc code=start
import string
VOWELS = {"a", "e", "i", "o", "u"}
CONSONANTS = set(string.ascii_lowercase).difference(VOWELS)

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        has_vowel = False
        has_consonant = False
        for char in word.lower():
            if char in VOWELS:
                has_vowel = True
            elif char in CONSONANTS:
                has_consonant = True
            elif str.isdigit(char):
                continue
            else:
                return False
        return has_consonant and has_vowel
            
        
# @lc code=end

