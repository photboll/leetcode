#
# @lc app=leetcode id=3557 lang=python3
#
# [3557] Find Maximum Number of Non Intersecting Substrings
#

# @lc code=start
from collections import defaultdict
class Solution:
    def maxSubstrings(self, word: str) -> int:

        res = 0
        previ = defaultdict(int)
        
        
        for i, char in enumerate(word):
            if char not in previ:
                previ[char] = i
            
            #the char needs to be atleast four spaces apart
            elif i >= previ[char] + 3:
                #we clear the dict to avoid counting intersecting chars
                previ.clear()
                res += 1
            
        return res
        
            


        
# @lc code=end

