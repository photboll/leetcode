#
# @lc app=leetcode id=3228 lang=python3
#
# [3228] Maximum Number of Operations to Move Ones to the End
#

# @lc code=start
class Solution:
    def maxOperations(self, s: str) -> int:

        """
        always choosing the rightmost 1 is optimal 
        """
        res = 0
        
        ones = 0
        n = len(s)
        for i in range(n):
            if s[i] == "1":
                ones += 1
            else:
                if i == 0 or s[i-1] == "1":
                    res += ones
            
        
        return res
# @lc code=end

