#
# @lc app=leetcode id=1975 lang=python3
#
# [1975] Maximum Matrix Sum
#

# @lc code=start
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        negative_count = 0
        min_abs_val = float("inf")

        for row in matrix:
            for val in row:
                total += abs(val)
                min_abs_val = min(min_abs_val, abs(val))
                if val < 0:
                    negative_count += 1
        
        if negative_count % 2 == 1:
            #times 2 because  we remove the addition of min_abs_val and then subtracts asnother
            total -= 2*min_abs_val

        return total
        
# @lc code=end

