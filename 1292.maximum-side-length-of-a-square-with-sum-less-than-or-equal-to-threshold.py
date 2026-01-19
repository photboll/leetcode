#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#

# @lc code=start
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """  
        binary search on side lengths?
        prefix sum, maybe to quickly find the total sum of particular square?
        """
        m = len(mat)
        n = len(mat[0])
        #contains the sum of the sub matric starting at 0, 0 and ending at i, j
        PS = [[0] * (n+1)for _ in range(m+ 1)]

        for i in range(m):
            for j in range(n):
                PS[i+1][j+1] = (
                    mat[i][j]
                    + PS[i][j+1]
                    + PS[i+1][j]
                    - PS[i][j]
                )
                
        def submatrix_sum(r1, c1, r2, c2):
            return (
                PS[r2+1][c2+1]
                - PS[r1][c2+1]
                - PS[r2+1][c1]
                + PS[r1][c1]
            )
        
        def any_subsquares_le(side):
            for i in range(len(PS)-side):
                for j in range(len(PS[0])-side):
                    s = submatrix_sum(i, j, i+side-1, j+side-1)
                    #print(i, j, s, side)
                    if s <= threshold:
                        return True
            return False
            

        lo = 0
        hi = min(m, n)

        while lo < hi:
            mid = lo + (hi - lo + 1)//2
            if any_subsquares_le(mid):
                lo = mid
            else:
                hi = mid -1
        return lo

        
# @lc code=end

