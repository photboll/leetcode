# @lc app=leetcode id=940 slug=distinct-subsequences-ii lang=python3
#
# [940] Distinct Subsequences II
# Difficulty: Hard
# Tags: String, Dynamic Programming
# URL: https://leetcode.com/problems/distinct-subsequences-ii/
#
# @lc code=start
from collections import defaultdict
MOD = pow(10, 9) + 7
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n +1)
        #dp = distinctsubseq(s[:i])
        last_occurence = {}

        for i in range(n):
            if s[i] not in last_occurence:#new char
                #then we appending the new char to each previous distint subsequence gives a new 
                #distinct subsequnece 
                #+1 for the case where only s[i] is included(appended to empty subseq)
                dp[i+1] = (dp[i] * 2 +1 )% MOD
            else:
                prev = last_occurence[s[i]]
                #we cant just take the previous value since it will include duplicates
                #how do i exclude the overlap?
                #it should be dp[last_occurence -1]

                dp[i+1] = (dp[i] * 2 - dp[prev]) % MOD
            
            last_occurence[s[i]] = i
            
        return dp[-1]

                
            



        

# @lc code=end
