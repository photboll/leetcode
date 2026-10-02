# @lc app=leetcode id=22 slug=generate-parentheses lang=python3
#
# [22] Generate Parentheses
# Difficulty: Medium
# Tags: String, Dynamic Programming, Backtracking, Bracket Sequences
# URL: https://leetcode.com/problems/generate-parentheses/
#
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        curr = []

        def dfs(open, close):
            if open == close == 0:
                result.append("".join(curr))

            if open > 0:
                curr.append("(")
                dfs(open -1, close)
                curr.pop()
            if close > open:
                curr.append(")")
                dfs(open, close -1)
                curr.pop()
        dfs(n, n)
        return result 

                

        

# @lc code=end
