#
# @lc app=leetcode id=3225 lang=python3
#
# [3225] Maximum Score From Grid Operations
#

# @lc code=start
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1:
            return 0
        
        #prefix sum per column
        col = [[0] * (n+1) for _ in range(m)]

        for j in range(m):
            for i in range(n):
                col[j][i+1] = col[j][i] + grid[i][j]

        dp = [[0] * (n+1) for _ in range(n+1)]
        pref_max = [[0]*(n+1) for _ in range(n+1)]
        suff_max = [[0]*(n+1) for _ in range(n+1)]

        for c in range(1, m):
            next_dp = [[0] * (n+1) for _ in range(n+1)]

            for curr in range(n+1):
                for prev in range(n+1):
                    if curr <= prev:
                        gain = col[c][prev] - col[c][curr]
                        next_dp[curr][prev] = max(
                            next_dp[curr][prev],
                            suff_max[prev][0] + gain
                        )
                    else:
                        gain = col[c-1][curr] - col[c-1][prev]
                        next_dp[curr][prev] = max(next_dp[curr][prev],
                                                  suff_max[prev][curr], 
                                                  pref_max[prev][curr] + gain
                                                   )
            # build prefix and suffix sum arrays
            for curr in range(n+1):

                pref_max[curr][0] = next_dp[curr][0]

                for prev in range(1, n+1):
                    penalty = 0
                    if prev > curr:
                        penalty = col[c][prev] - col[c][curr]

                    pref_max[curr][prev] = max(
                        pref_max[curr][prev-1],
                        next_dp[curr][prev] - penalty
                    )

                suff_max[curr][n] = next_dp[curr][n]

                for prev in range(n-1, -1, -1):
                    suff_max[curr][prev] = max(
                        suff_max[curr][prev+1],
                        next_dp[curr][prev]
                    )

            dp = next_dp

        ans = 0
        for k in range(n+1):
            ans = max(ans, dp[0][k], dp[n][k])

        return ans
        
# @lc code=end

