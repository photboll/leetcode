#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """ 
        DP? triangular matrix
        start with pouring x into dp[i][j], x - 1 will move over to the next row
        the remainder will flow over to dp[i+1][j] and dp[i+1][j+1]
        
        """
        dp = [[0] * (query_row+2) for _ in range(query_row+2)]
        dp[0][0] = poured
        #print("_"*10)
        #print(poured, query_row, query_glass)
        for r in range(query_row+1):
            for c in range(r+1):
                if dp[r][c] >= 1:
                    #the rest overflows to the next row
                    overflow = (dp[r][c] - 1) / 2
                    dp[r+1][c] += overflow
                    dp[r+1][c+1] += overflow
                    dp[r][c] = 1# one cup stays

            #print(dp[r])


        return dp[query_row][query_glass]


        
# @lc code=end

