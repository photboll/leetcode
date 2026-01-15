#
# @lc app=leetcode id=2943 lang=python3
#
# [2943] Maximize Area of Square Hole in Grid
#

# @lc code=start
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        def longest_seq_consecutive_ints(bars):
            bars.sort()
            res = 1
            cur = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    cur += 1
                else:
                    cur = 1
                res = max(res, cur)
            return res
        
        side = min(longest_seq_consecutive_ints(vBars),
                   longest_seq_consecutive_ints(hBars),
                   ) + 1
        return side * side
            
        
# @lc code=end

