#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        suffix_sum = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]
        
        dp = [[0]* (n+1) for _ in range(n+1)]
        #if M == n then the current player can take all piles 
        #which is always optimal
        for i in range(n-1, -1, -1):
            dp[i][n] = suffix_sum[i]

        for idx in range(n-1, -1, -1):
            for M in range(n-1, 0, -1):
                for X in range(1, min(2*M, n-idx)+1):
                    dp[idx][M] = max(
                        dp[idx][M],
                        suffix_sum[idx] - dp[idx+X][max(M, X)]
                    )

        return dp[0][1]
                
        


        
# @lc code=end

