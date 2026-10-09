# @lc app=leetcode id=1541 slug=minimum-insertions-to-balance-a-parentheses-string lang=python3
#
# [1541] Minimum Insertions to Balance a Parentheses String
# Difficulty: Medium
# Tags: String, Stack, Greedy, Bracket Sequences
# URL: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
#
# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        result = 0
        opens = 0
        i = 0

        while i < n:
            if s[i] == "(":
                opens += 1
            
            elif s[i] == ")" and i+1< n and s[i+1] == ")":
                i += 1
                if opens > 0:
                    opens -= 1
                else:# need to balance with another opening
                    result += 1
            
            elif s[i] == ")":#only one closing, we need to balance with another closing
                result += 1
                if opens > 0:
                    opens -= 1
                else:#need another open to match 
                    result += 1
            
            i += 1
        
        result += 2 * opens
        return result 
        
        
            
            


        

# @lc code=end
