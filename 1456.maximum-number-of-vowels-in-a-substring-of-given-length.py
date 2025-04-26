#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
VOWELS = set(["a", "e","i","o","u"])
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_in_window = 0
        n = len(s)
        for i in range(k):
            if s[i] in VOWELS:
                vowels_in_window += 1
                
        max_vowels = vowels_in_window
        for i in range(k, n):
            vowels_in_window += (s[i] in VOWELS)
            vowels_in_window -= (s[i-k] in VOWELS)
            max_vowels = max(vowels_in_window, max_vowels)
            
        return max_vowels 
            
        
# @lc code=end

