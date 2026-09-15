# @lc app=leetcode id=3414 slug=maximum-score-of-non-overlapping-intervals lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
# Difficulty: Hard
# Tags: Array, Binary Search, Dynamic Programming, Sorting
# URL: https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/
#
# @lc code=start
from bisect import *
NUM_CHOICES = 4

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = [[start, end, weight, i]
            for i, (start, end, weight) in enumerate(intervals)
        ]
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        dp = [[0] * n for _ in range(NUM_CHOICES + 1)]
        chosen = [[()] * n for _ in range(NUM_CHOICES + 1)]  # sorted tuple of original indices

        endpoints = [x[1] for x in intervals]

        for k in range(1, NUM_CHOICES + 1):
            for i in range(n):
                j = bisect_left(endpoints, intervals[i][0], lo=0, hi=i) - 1

                pick = intervals[i][2]
                pick_idx = (intervals[i][3],)
                if j >= 0:
                    pick += dp[k - 1][j]
                    pick_idx = tuple(sorted(chosen[k - 1][j] + pick_idx))

                skip = dp[k][i - 1] if i > 0 else 0
                skip_idx = chosen[k][i - 1] if i > 0 else ()

                if pick > skip or (pick == skip and pick_idx < skip_idx):
                    dp[k][i] = pick
                    chosen[k][i] = pick_idx
                else:
                    dp[k][i] = skip
                    chosen[k][i] = skip_idx

        return list(chosen[NUM_CHOICES][n - 1]) if n else []

        

        

# @lc code=end
