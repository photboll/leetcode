#
# @lc app=leetcode id=1411 lang=python3
#
# [1411] Number of Ways to Paint N × 3 Grid
#

# @lc code=start
MOD = pow(10, 9) + 7
class Solution:
    def numOfWays(self, n: int) -> int:
        #n == 1
        x = 6# There are 6 ways to color using 2 colors
        y = 6# there are 6 ways to color using 3 colors
        
        for i in range(2, n+1):
            #if the previous row was a 2 color combo
            #then: 3 options for 2 color combo and 2 options of 3 color combo
            new_x = (3 * x + 2* y) % MOD
            #if previous was a 3 color combo
            #then: 2 options for 2 color combo and 2 options for 3 color combo
            new_y = (2 * x + 2*y) % MOD
            x = new_x
            y = new_y

        
        return (x + y) % MOD
# @lc code=end

