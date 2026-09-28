# @lc app=leetcode id=1614 slug=maximum-nesting-depth-of-the-parentheses lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
# Difficulty: Easy
# Tags: String, Stack, Bracket Sequences
# URL: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
#
# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        result = 0

        for char in s:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            
            if depth > result:
                result = depth
        return result 
        
    
            
            
        

# @lc code=end
