# @lc app=leetcode id=32 slug=longest-valid-parentheses lang=python3
#
# [32] Longest Valid Parentheses
# Difficulty: Hard
# Tags: String, Dynamic Programming, Stack, Bracket Sequences
# URL: https://leetcode.com/problems/longest-valid-parentheses/
#
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        result = 0

        for i in range(len(s)):
            if s[i] == "(":
                #possible starting point 
                stack.append(i)
            else:
                #Closing paranthese
                stack.pop()

                if stack:
                    result = max(result, i - stack[-1])
                else:
                    stack.append(i)
        
        return result


class SolutionV1:
    def longestValidParentheses(self, s: str) -> int:
        """
        this is a wrong approach 
        sliding window, two pointers 
        if open == close then it is a valid substring 
        if close > open then make the window smaller

        """
        result = 0
        n = len(s)
        if n < 2:
            return 0
        open = 0
        close = 0
        l = 0

        for r in range(n):
            if s[r] == "(":
                open += 1
            elif s[r] == ")":
                close += 1
            
            while close > open :
                if s[l] == "(":
                    open -= 1
                elif s[l] == ")":
                    close -= 1
                l += 1
            
            if open == close and r -l + 1 > result:
                result = r - l + 1

        while l < r:
            if s[l] == "(":
                open -= 1
            elif s[l] == ")":
                close -= 1
            l += 1

            if open == close and r -l + 1 > result:
                result = r - l + 1
        
        
        
        return result
                

                


            
        
        

# @lc code=end
