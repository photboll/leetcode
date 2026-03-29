#
# @lc app=leetcode id=2906 lang=python3
#
# [2906] Construct Product Matrix
#

# @lc code=start

MOD = 12345

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        prefix = [[1]* n for _ in range(m)]
        suffix = [[1]* n for _ in range(m)]
        result = [[1]* n for _ in range(m)]

        pref = 1
        for r in range(m):
            for c in range(n):
                prefix[r][c] = pref 
                pref *= (grid[r][c] % MOD)
        
        suff = 1
        for r in range(m-1, -1,-1):
            for c in range(n-1, -1,-1):
                suffix[r][c] = suff
                suff *= (grid[r][c] % MOD)
        #print(prefix)
        #print(suffix)

        
        for r in range(m):
            for c in range(n):
                result[r][c] = (suffix[r][c] * prefix[r][c] ) % MOD
        return result

                
                



        
# @lc code=end

