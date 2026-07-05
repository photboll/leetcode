#
# @lc app=leetcode id=1301 lang=python3
#
# [1301] Number of Paths with Max Score
#

# @lc code=start
MOD = pow(10, 9) + 7
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)

        dp = [[[-1, 0]] * n for _ in range(n)]

        dp[n-1][n-1] = [0, 1]

        def update(x, y, u, v):
            #out of bounds?
            if u >= n or v >= n or dp[u][v][0] == -1:
                return

            #is there a new max?
            if dp[u][v][0] > dp[x][y][0]:
                dp[x][y] = dp[u][v][:]
            #both paths lead to the same sum increase the max sum
            elif dp[u][v][0] == dp[x][y][0]:
                dp[x][y][1] += dp[u][v][1]

            
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if not (i == n-1 and j == n-1) and board[i][j] != "X":

                    update(i, j, i+1, j)#down
                    update(i, j, i, j+1)#right
                    update(i, j, i+1, j+1)#diagonal
                    
                    
                    if dp[i][j][0] != -1 and board[i][j] != "E":
                        #E adds no value so skip it
                        dp[i][j][0] = (
                            dp[i][j][0] +\
                            int(board[i][j])
                        ) % MOD
        
        if dp[0][0][0] == -1:
            return [0, 0]
        else:
            return [dp[0][0][0], dp[0][0][1] % MOD]
        
# @lc code=end

