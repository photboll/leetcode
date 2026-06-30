#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
#

# @lc code=start
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        substrs = set()
        n = len(word)
        for i in range(n):
            for j in range(i+1, n):
                substrs.add(word[i:j+1])

        res = 0
        for pattern in patterns:
            if pattern in substrs:
                res += 1

        return res 
                
        
# @lc code=end

