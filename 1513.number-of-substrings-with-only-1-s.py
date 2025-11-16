#
# @lc app=leetcode id=1513 lang=python3
#
# [1513] Number of Substrings With Only 1s
#

# @lc code=start
MOD = pow(10, 9)+7
class Solution:
    def numSub(self, s: str) -> int:
        def num_substrings(n):
            return (n*(n+1) // 2) % MOD
        
        res = 0
        ones = 0
        for i in range(len(s)):
            if s[i] == "1":
                ones += 1
            else:
                res += num_substrings(ones) % MOD
                ones = 0
        
        res += num_substrings(ones) % MOD
        return res

            
            
            
        
# @lc code=end

