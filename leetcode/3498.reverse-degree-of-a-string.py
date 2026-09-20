# @lc app=leetcode id=3498 slug=reverse-degree-of-a-string lang=python3
#
# [3498] Reverse Degree of a String
# Difficulty: Easy
# Tags: String, Simulation
# URL: https://leetcode.com/problems/reverse-degree-of-a-string/
#
# @lc code=start
from string import ascii_lowercase

c2val = {c:26-i for i, c in enumerate(ascii_lowercase)}

class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0

        for i, char in enumerate(s):
            result += (i+1) * c2val[char]
        return result
        

# @lc code=end
