#
# @lc app=leetcode id=2839 lang=python3
#
# [2839] Check if Strings Can be Made Equal With Operations I
#

# @lc code=start
from collections import Counter
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        evens = Counter([val for val in s1[::2]])
        odds = Counter([val for val in s1[1::2]])

        for i, val in enumerate(s2):
            if i % 2 == 0:
                evens[val] -= 1
            else:
                odds[val] -= 1
        
        for v in evens.values():
            if v != 0:
                return False
        
        for v in odds.values():
            if v != 0:
                return False
        return True



        
# @lc code=end

