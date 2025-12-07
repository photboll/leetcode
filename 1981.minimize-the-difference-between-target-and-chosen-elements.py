#
# @lc app=leetcode id=1981 lang=python3
#
# [1981] Minimize the Difference Between Target and Chosen Elements
#

# @lc code=start
from functools import cache

class SolutionV1:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        mat = [set(row) for row in mat]
        rSet = set(mat.pop())
        for row in mat:
            rSet = {m+n for m in row for n in rSet}
        return min(abs(n-target) for n in rSet)

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """
        all numbers are positive. so it the ssum will be strictly increasing 

        """
        m = len(mat)
        min_suffix = [0] * (m+1)
        for i in range(m-1, -1,-1):
            mat[i].sort()
            min_suffix[i] = min_suffix[i+1] + mat[i][0]

        result = [float("inf")]

        
        @cache
        def dfs(row, s):
            lb_diff = (abs(s + min_suffix[row]) - target)
            if lb_diff > result[0]:   
                return float("inf")
            if row == m:
                diff = abs(s -target)
                result[0] = min(result[0], diff)
                return diff


            best_diff = float("inf")
            for num in mat[row]:
                diff = dfs(row+1, num + s)
                best_diff = min(best_diff, diff)
                if best_diff == 0:
                    return best_diff
            return best_diff
            
        return dfs(0,0)


                
        
# @lc code=end

