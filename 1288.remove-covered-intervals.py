#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))

        result = 0
        last_endpoint = 0

        for _, end in intervals:
            if end > last_endpoint:
                result += 1
                last_endpoint = end
        return result

                


        
# @lc code=end

