#
# @lc app=leetcode id=2929 lang=python3
#
# [2929] Distribute Candies Among Children II
#

# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        tot = 0
        
        for i in range(min(n, limit)+1):
            #THe first child get i candies
            tot += max(min(limit, n-i) - max(0, n-i-limit)+1, 0)
    
        return tot
        
# @lc code=end

