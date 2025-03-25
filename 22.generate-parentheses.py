#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(cntOpen, cntClosed,  order):
            if cntOpen == n and cntClosed == n:
               result.append("".join(order))

            if cntOpen < n:
                backtrack(cntOpen + 1, cntClosed,   order + ["("])
                
            if cntClosed < n and cntClosed < cntOpen:
                backtrack(cntOpen, cntClosed+1,  order + [")"])
        
        backtrack(0, 0, [])
        return result        
# @lc code=end

