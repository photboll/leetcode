# @lc app=leetcode id=3870 slug=count-commas-in-range lang=python3
#
# [3870] Count Commas in Range
# Difficulty: Easy
# Tags: Math
# URL: https://leetcode.com/problems/count-commas-in-range/
#
# @lc code=start
class Solution:
    def countCommas(self, n: int) -> int:
        #the first thousnd numbers have no comma
        #and all after that have one comma since 1<= n <= 100000
        if n < 1000:
            return 0
        else:
            return n - 999
        

# @lc code=end
