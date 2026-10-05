# @lc app=leetcode id=856 slug=score-of-parentheses lang=python3
#
# [856] Score of Parentheses
# Difficulty: Medium
# Tags: String, Stack, Bracket Sequences
# URL: https://leetcode.com/problems/score-of-parentheses/
#
# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        score = 0
        depth = 0

        for i in range(n):
            if s[i] == "(":
                depth += 1
            else:
                depth -= 1
                if s[i-1] == "(":
                    score += 1 << depth
        return score


        

    
        

# @lc code=end
