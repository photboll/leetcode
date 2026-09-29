# @lc app=leetcode id=2267 slug=check-if-there-is-a-valid-parentheses-string-path lang=python3
#
# [2267]  Check if There Is a Valid Parentheses String Path
# Difficulty: Hard
# Tags: Array, Dynamic Programming, Matrix, Bracket Sequences
# URL: https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
#
# @lc code=start

MAX_PATH_LEN = 110

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        """
        is it enough for the number of opening parantheses to be the same as closing?
        Yes. As long as there is only one type of paranthese

        only down or right 

        dp only keeping the open - close?
        no that is not enough. 

        one more dimension k? where k = open - close 
        dp[r][c][k] = number of balanced paths ending at (r,c) with open-close == k
        if open - close < 0 we can prune since it cant turn into a valid path a later stage
        dp[-1][-1][0] will then hold the answer

        
        we actually dont need to have the row dimension since we are only ever looking to r-1
        
        """
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != "(":
            return False

        dp = [[[False] * MAX_PATH_LEN for _ in range(n)] for _ in range(m)]
        
        dp[0][0][1] = True

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                delta = 1 if grid[r][c] == "(" else -1
                for k in range(MAX_PATH_LEN):
                    prev = k - delta
                    if prev < 0 or prev >= MAX_PATH_LEN:
                        continue
                    if (r > 0 and dp[r-1][c][prev]) or (c > 0 and dp[r][c-1][prev]):
                        dp[r][c][k] = True

        return dp[-1][-1][0]
            



        



        

        

# @lc code=end
