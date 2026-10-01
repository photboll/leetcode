# @lc app=leetcode id=20 slug=valid-parentheses lang=python3
#
# [20] Valid Parentheses
# Difficulty: Easy
# Tags: String, Stack, Bracket Sequences
# URL: https://leetcode.com/problems/valid-parentheses/
#
# @lc code=start
O2C = {}#Open 2 Close 
C2O = {}#Close 2 Open
for o, c in ["()", "[]", "{}"]:
    O2C[o] = c
    C2O[c] = o
    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        #Nice comment

        for char in s:
            if char in O2C:
                stack.append(char)
            elif char in C2O and stack and C2O[char] == stack[-1]:
                stack.pop()
            elif char in C2O:
                return False
            
            


        return len(stack) == 0



            
            
            
            
        
        

                
        

# @lc code=end
