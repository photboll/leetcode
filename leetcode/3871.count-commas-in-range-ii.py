# @lc app=leetcode id=3871 slug=count-commas-in-range-ii lang=python3
#
# [3871] Count Commas in Range II
# Difficulty: Medium
# Tags: Math
# URL: https://leetcode.com/problems/count-commas-in-range-ii/
#
# @lc code=start
class Solution:
    def countCommas(self, n: int) -> int:
        #1000 to 999999 one comma
        #1000000 to 999999999 two comma
        k = 1000
        result = 0

        while k <= n:
            result += n - k + 1
            k *= 1000
        return result 
            




        

# @lc code=end
