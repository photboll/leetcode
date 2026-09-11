# @lc app=leetcode id=3483 slug=unique-3-digit-even-numbers lang=python3
#
# [3483] Unique 3-Digit Even Numbers
# Difficulty: Easy
# Tags: Array, Hash Table, Recursion, Enumeration
# URL: https://leetcode.com/problems/unique-3-digit-even-numbers/
#
# @lc code=start
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        """
        even number last digit must be an een digit rest can be chosen freely

        """
        counts = [0] * 10

        for digit in digits:
            counts[digit] += 1

        result = 0

        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):
                    if (counts[a] >= 1
                        and counts[b] - (b == a) >= 1
                        and counts[c] - (c == a) - (c == b) >= 1):
                        result += 1
        return result

        
        
        

# @lc code=end