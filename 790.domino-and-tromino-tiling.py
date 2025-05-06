#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start


MOD = pow(10, 9) + 7
class Solution:
    def numTilings(self, n: int) -> int:
        """
        2* n so
        we should be able to dp it, 
        n=1 -> 1 one vertical domino
        n=2 -> 2 two vertical or two horiontal 
        3   -> 5
        we can extend all n-1 solutions with a single vertical domino, n=3 2 such cases 
        we can extend the n-2 solutions with a double horizontal domino, n=3 1 case
        We can extend the n-3 solutions with two different versions of trominos, n=3 2 cases
        """
        dp = [0] * max(3, (n + 1))
        dp[0], dp[1], dp[2] = 1, 1, 2
        
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
            
        return dp[n]
    

        
# @lc code=end

