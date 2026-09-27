# @lc app=leetcode id=1190 slug=reverse-substrings-between-each-pair-of-parentheses lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
# Difficulty: Medium
# Tags: String, Stack, Bracket Sequences
# URL: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
#
# @lc code=start
from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_idxs = []
        pair = [0] * n

        #First pass> pair parantheses
        for i in range(n):
            if s[i] == "(":
                open_idxs.append(i)
            if s[i] == ")":
                j = open_idxs.pop()
                pair[i] = j
                pair[j] = i

        result = []
        curr = 0
        direction = 1

        while curr < n:
            if s[curr] == "(" or s[curr] == ")":
                curr = pair[curr]
                direction = -direction
            else:
                result.append(s[curr])
            curr += direction

        return "".join(result)

class SolutionV1:
    def reverseParentheses(self, s: str) -> str:
        """
        nested parntheses.
        
        stack approach or recursive approach?
        recursive probably shorter but harder to reason about 
        maybe a stack of stacks?

        opening paranthese start a new stack 
        closing paranthese pop from stack and append to stack above 
        
        """
        open_idxs = deque()
        result = []
        for char in s:
            if char == "(":
                open_idxs.append(len(result))
            elif char == ")":
                start = open_idxs.pop()
                result[start:] = reversed(result[start:])
            else:
                result.append(char)

        return "".join(result)
            
        
        

# @lc code=end
