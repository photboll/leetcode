# @lc app=leetcode id=3723 slug=maximize-sum-of-squares-of-digits lang=python3
#
# [3723] Maximize Sum of Squares of Digits
# Difficulty: Medium
# Tags: Math, Greedy
# URL: https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
#
# @lc code=start
class Solution:
    def maxSumOfSquares(self, num: int, s: int) -> str:
        """
        start with num 9s 

        the order of the digits does not matter

        """
        result = []

        while len(result) < num:
            digit = min(9, s)
            result.append(str(digit))
            s -= digit
        
        if s:
            return ""
        else:
            return "".join(result)

        

# @lc code=end
