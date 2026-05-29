#
# @lc app=leetcode id=3121 lang=python3
#
# [3121] Count the Number of Special Characters II
#

# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = [-1] * 30
        first_upper = [-1] * 30

        for i, c in enumerate(word):
            idx = ord(c.lower()) - ord("a") 
            if c.islower():
                last_lower[idx] = i
            elif first_upper[idx] < 0 and c.isupper():
                first_upper[idx] = i
        
        res = 0

        for ll, fu in zip(last_lower, first_upper):
            if 0<= ll < fu:
                res += 1

        return res 
                

    
        
# @lc code=end

