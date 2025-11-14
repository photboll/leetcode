#
# @lc app=leetcode id=2536 lang=python3
#
# [2536] Increment Submatrices by One
#

# @lc code=start
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        pref_sum = [[0]*(n+1)for _ in range(n+1)]

        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2+1):
                pref_sum[r][c1] += 1
                pref_sum[r][c2+1] -= 1
                
        res = [[0] *n for _ in range(n)]
        for r in range(n):
            cur_val = 0
            for c in range(n):
                cur_val += pref_sum[r][c]
                res[r][c] = cur_val
        return res
            
            
        
# @lc code=end

