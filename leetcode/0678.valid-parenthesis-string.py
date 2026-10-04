# @lc app=leetcode id=678 slug=valid-parenthesis-string lang=python3
#
# [678] Valid Parenthesis String
# Difficulty: Medium
# Tags: String, Dynamic Programming, Stack, Greedy, Bracket Sequences
# URL: https://leetcode.com/problems/valid-parenthesis-string/
#
# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        opens = []
        stars = []

        for i, c in enumerate(s):
            if c == "(":
                opens.append(i)
            elif c == "*":
                stars.append(i)
            else:#closing
                if opens: # match against opening bracket
                    opens.pop()
                elif stars: # match against wildcard
                    stars.pop()
                else:
                    return False
        
        while opens and stars:
            if opens[-1] < stars[-1]:# close the opening with a star
                opens.pop()
                stars.pop()
            else:
                return False
        
        return len(opens) == 0
        
        
                
                
            
            


        

# @lc code=end
