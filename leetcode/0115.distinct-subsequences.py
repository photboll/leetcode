# @lc app=leetcode id=115 slug=distinct-subsequences lang=python3
#
# [115] Distinct Subsequences
# Difficulty: Hard
# Tags: String, Dynamic Programming
# URL: https://leetcode.com/problems/distinct-subsequences/
#
# @lc code=start
from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) +1)
        dp[0] = 1

        for char in s:
            for i in range(len(t), 0, -1):
                if char == t[i-1]:
                    dp[i] += dp[i-1]

        return dp[-1]

class SolutionV1:
    def numDistinct(self, s: str, t: str) -> int:
        """
        s = "rabbbit", t = "rabbit"
        for each i, char in the target string s;
        if char is in t. maybe we need to do it for each one. so in exampe one there will be 3 * 2 total runs?
        but how wont i double count? do i always take the middle element?

        total += 
        ways to make the prefix up to i * 1 * ways to make the suffix after i
        is this not recursive of the same problem?
        """

        @cache
        def dp(s, t):
            if len(t) == 0:
                return 1
            if len(s) == 0:
                return 0
            elif len(t) == 1:
                return s.count(t)
            

            mid = len(t) // 2
            total = 0
            for i, char in enumerate(s):
                if char == t[mid]:
                    total += (\
                        dp(s[:i], t[:mid]) * # ways to make prefix of t to the left of i
                        dp(s[i+1:], t[mid+1:])#ways to make suffix of t to the right of i
                    )
            #print(s, t, total)
            return total
        
        return dp(s, t)
            
            
            
                
        
        

# @lc code=end
