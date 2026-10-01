# @lc app=leetcode id=1111 slug=maximum-nesting-depth-of-two-valid-parentheses-strings lang=python3
#
# [1111] Maximum Nesting Depth of Two Valid Parentheses Strings
# Difficulty: Medium
# Tags: String, Stack, Bracket Sequences
# URL: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
#
# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        """
        maybe assign a rank equal to the depth of each bracket is responsible for
        
        start with A = seq
        then move the two brackets with the highest rank to B. Check what Bs depth is and continue if it improved
        
        is it true that if we always move them pairwise to B. we will always have B as a VPS 
        I htink yes, 
        
        """
        result = []
        depth = 0
        for char in seq:
            if char == "(":
                depth += 1
                result.append(depth % 2 )
            if char == ")":
                result.append(depth % 2 )
                depth -= 1
        return result
        

        
        

# @lc code=end
