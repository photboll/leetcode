# @lc app=leetcode id=921 slug=minimum-add-to-make-parentheses-valid lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
# Difficulty: Medium
# Tags: String, Stack, Greedy, Bracket Sequences
# URL: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
#
# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        inserts = 0
        open = 0

        for char in s:
            if char == "(":
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:# we need to insert an opening
                    inserts += 1

        return inserts + open
            


class SolutionWRONG:
    def minAddToMakeValid(self, s: str) -> int:
        """
        maybe it is enough to just count them 
        it is not enough 
        """
        counts = [0, 0]

        for char in s:
            counts[ord(char) - ord("(")] += 1
        
        mn = min(counts)
        mx = max(counts)
        return mx - mn 

        
        

# @lc code=end
