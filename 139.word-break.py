#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakRecursive(s, frozenset(wordDict))
    
    @cache 
    def wordBreakRecursive(self, s:str, wordDict: frozenset[str]) -> bool:
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            if s[:i] in wordDict:
               isPossible = self.wordBreakRecursive(s[i:], wordDict) 
               if isPossible:
                   return True
            
        return False
# @lc code=end

