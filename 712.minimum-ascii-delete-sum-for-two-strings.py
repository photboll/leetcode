#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

# @lc code=start
from functools import cache
from string import ascii_lowercase

c2val = {c:i+97 for i, c in enumerate(ascii_lowercase)}
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        
        @cache
        def dp(i, j):
            if i >= m and j>= n:
                return 0
            if i >= m:
                return sum(c2val[s2[k]] for k in range(j, n))
            if j >= n:
                return sum(c2val[s1[k]] for k in range(i, m))
            
            #3 choices
            #1. both chars match, move forward without deleting any
            # is ther every any reason to ignoe a match?
            #2. skip char in s1, i+1
            #3. skip char in s2, j+1
            
            if s1[i] == s2[j]:
                return dp(i+1, j+1)
            
            skip1 = dp(i+1, j) + c2val[s1[i]]
            skip2 = dp(i, j+1) + c2val[s2[j]]
            return min(skip1, skip2)
        
        return dp(0, 0)   
            
        
# @lc code=end

