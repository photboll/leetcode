# @lc app=leetcode id=1807 slug=evaluate-the-bracket-pairs-of-a-string lang=python3
#
# [1807] Evaluate the Bracket Pairs of a String
# Difficulty: Medium
# Tags: Array, Hash Table, String
# URL: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
#
# @lc code=start
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know = {row[0]: row[1] for row in knowledge} 
        chars = []
        result = []

        for char in s:
            if char == ")":
                key = "".join(chars)
                print(key)
                result.append(know.get(key, "?"))
                chars.clear()
            elif char == "(":
                result.append("".join(chars))
                chars.clear()
            else:
                chars.append(char)

        result.extend(chars)
        return "".join(result)
                
        

# @lc code=end
