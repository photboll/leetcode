#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[n-1] = questions[n-1][0]#With a single question the bst option is to do it 
        
        for i in range(n-2, -1, -1):
            skip_i = dp[i+1]
            if i + 1 + questions[i][1] >= n:
                #This will be the last quesition
                do_i = questions[i][0]
            else:
                do_i = questions[i][0] + dp[i + 1+ questions[i][1]]
            
            dp[i] = max(skip_i, do_i)
        
        return dp[0] 
# @lc code=end

