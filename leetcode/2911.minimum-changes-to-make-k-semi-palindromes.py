# @lc app=leetcode id=2911 slug=minimum-changes-to-make-k-semi-palindromes lang=python3
#
# [2911] Minimum Changes to Make K Semi-palindromes
# Difficulty: Hard
# Tags: Two Pointers, String, Dynamic Programming
# URL: https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/
#
# @lc code=start
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        n = len(s)

        
        # divisors 
        divs = [[] for _ in range(n+1)]
        for d in range(1, n):
            for L in range(2 * d, n+1, d):
                divs[L].append(d)



        INF = float("inf")
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                L = j-i+1
                best = INF
                for d in divs[L]:
                    #number of elements per group
                    m = L // d 
                    c = 0
                    for r in range(d):
                        lo, hi = i+r, i+r+(m-1)*d
                        while lo < hi:
                            if s[lo] != s[hi]:
                                c += 1
                            lo += d
                            hi -= d
                    best = min(best, c)
                cost[i][j] = best


        #dp[p][j]: first j chars split into p parts
        dp = [[INF] * (n+1) for _ in range(k+1)]
        dp[0][0] = 0
        for p in range(1, k+1):
            for j in range(2*p, n+1):
                for i in range(2*(p-1), j-1):
                    if dp[p-1][i] < INF:
                        v = dp[p-1][i] + cost[i][j-1]
                        if v < dp[p][j]:
                            dp[p][j] = v
        #print(cost)
        #print(dp)
        return dp[k][n]


# @lc code=end
