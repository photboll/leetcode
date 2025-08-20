#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#

# @lc code=start


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        DP approach where we count the number of squares with the bottom right corner in i, j
        
        we need to keep a running count of the total number of submatrices with all ones
        
        do i need two matrix sized objects to store temporary infromation, one keeping track of the total counts of submatrices with all ones 
        and one to keep track of the largest square seen ending here.
        the first one do not actually have to be matrix it can just be a total count
        
        if we have a 1 at i,j: and all three previous positions (i-1, j-1), (i-1, j), (i, j-1) have a maximum of size k
        then we will have a square of k+1 ending here
         
        
        """
        m = len(matrix)
        n = len(matrix[0])

        #keep track of the largest square ending(bottom right corner) at i,j
        dp = [[0]*n for _ in range(m)]

        total = 0
        for i in range(m):
            if matrix[i][0] == 1:
                dp[i][0] = 1
                total += 1
        
        for j in range(1, n):
            if matrix[0][j] == 1:
                dp[0][j] = 1
                total += 1
        
        for i in range(1, m):
            for j in range(1, n):
                #What is the size of the largest square ending at i,j
                if matrix[i][j] == 0:
                    #if current position is 0 no square will end here
                    dp[i][j] = 0
                else:# current position is 1
                
                    dp[i][j] = 1#at least one square of size 1
                    k = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    #All previous positions have a square of  at least k
                    if k > 0:
                        #then the current position makes a new square of size k+1
                        dp[i][j] += k

                    #there is one square of each size from 1 to k ending at the current position
                    total += dp[i][j]
                    print(i, j, total, dp[i-1][j] == dp[i-1][j-1] == dp[i][j-1], dp[i][j-1])

        return total
        
# @lc code=end

