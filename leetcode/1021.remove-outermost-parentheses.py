# @lc app=leetcode id=1021 slug=remove-outermost-parentheses lang=python3
#
# [1021] Remove Outermost Parentheses
# Difficulty: Easy
# Tags: String, Stack, Bracket Sequences
# URL: https://leetcode.com/problems/remove-outermost-parentheses/
#
# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0

        result = []

        for char in s:
            if char == ")":
                depth -= 1
            if depth > 0:
                result.append(char)
            if char == "(":
                depth += 1

        return "".join(result)
        

# @lc code=end
