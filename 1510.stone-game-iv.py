#
# @lc app=leetcode id=1510 lang=python3
#
# [1510] Stone Game IV
#

# @lc code=start
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        #dp[i] is true if the current player can/will win
        dp = [False] * (n + 1)


        for i in range(1, n+1):
            k = 1
            while k *k <= i:
                if not dp[i-k*k]:
                    dp[i] = True
                    break
                k += 1

        return dp[n]

        
# @lc code=end

