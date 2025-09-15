#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)

        total = 0
        for word in text.split(" "):
            possible = True
            for c in word:
                if c in brokenLetters:
                    possible = False
                    break
            
            if possible:
                total += 1
                
        return total 
        
# @lc code=end

