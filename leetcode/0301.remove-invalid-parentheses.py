# @lc app=leetcode id=301 slug=remove-invalid-parentheses lang=python3
#
# [301] Remove Invalid Parentheses
# Difficulty: Hard
# Tags: String, Backtracking, Breadth-First Search
# URL: https://leetcode.com/problems/remove-invalid-parentheses/
#
# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []
        stack = [(s, 0, 0, ("(", ")"))]

        while stack:
            curr, li, lj, par = stack.pop()

            n = len(curr)
            balance = 0
            match = False

            for i in range(li, n):
                balance += (curr[i] == par[0]) - (curr[i] == par[1])
                if balance >= 0:
                    continue
                
                
                for j in range(lj, i+1):
                    if curr[j] == par[1] and (j == lj or curr[j-1] != par[1]):
                        nxt = curr[:j] + curr[j+1:]
                        stack.append((nxt, i, j, par))
                
                match = True
                break
            
            if not match:
                rev = curr[::-1]
                if par[0] == "(":
                    stack.append((rev, 0, 0, (")", "(")))
                else:
                    res.append(rev)
        return res

        

# @lc code=end
