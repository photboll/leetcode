#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #We want to use 2 dimensional DP array
        #It will have the same size as matrix
        #dp[i][j] will hold the size of the largest square that as its bottom right corner in i, j
        #NOTE: max SQUARE not RECTANGLE. even tohug the matrix itself is a rectangle 
        #if matrix[i][j] == 0 then the answer will remain the largest of its predecessors 
        #matix[i][j] == 1 have a chance of making making the square larger by 1
        #but it requires that the left, digonal and right element of the currentposition 
        #all have ATLEAST the same size of n-1 to make a square of n. 
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        #init the max square can at most be 1 along the edges 
        for i in range(len(matrix)):
            dp[i][0] = matrix[i][0] == "1"
        
        for j in range(len(matrix[0])):
            dp[0][j] = matrix[0][j] == "1"

            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        return max(map(max, dp))**2
# @lc code=end

