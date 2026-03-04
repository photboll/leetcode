#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row_sum = [0] * m
        col_sum = [0] * n

        for r in range(m):
            for c in range(n):
                row_sum[r] += mat[r][c]
                col_sum[c] += mat[r][c]
        res = 0
        for r in range(m):
            if row_sum[r] != 1:
                continue
            for c in range(n):
                if col_sum[c] == 1 and mat[r][c] == 1:
                    res += 1
        
        return res

                
        
# @lc code=end

