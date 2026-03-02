#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0 

        prev= 0
        s = bin(n)[:2]
        for i in range(len(s)):
            if s[i] == "1":
                res = max(res, i - prev)
                prev = i
        return res
            
        
# @lc code=end

