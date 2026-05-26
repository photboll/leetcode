#
# @lc app=leetcode id=3120 lang=python3
#
# [3120] Count the Number of Special Characters I
#

# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seenLower = [False] * 30
        seenUpper = [False] * 30
        res = 0

        for char in word:
            if char.islower():
                seenLower[ord(char) - ord("a")] = True
            elif char.isupper():
                seenUpper[ord(char.lower()) - ord("a")] = True

        for l, u in zip(seenLower, seenUpper):
            if l and u:
                res += 1
        return res
                
                
                
        
# @lc code=end

