#
# @lc app=leetcode id=1751 lang=python3
#
# [1751] Maximum Number of Events That Can Be Attended II
#

# @lc code=start
from bisect import bisect_right
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        We sort it based on the start time.
        If we choose to attend the current event, we gain value and we the next possible event we can attend is after endDay
        iw we choose to not attend the current event, we can possibly attend a "better" event in the mean time
        """
        
        events.sort()
        n = len(events)
        start_times = [event[0] for event in events]
        dp = [[-1] * n for _ in range(k+1)]
        
        def dfs(i, count):
            if count == 0 or i== n:
                return 0
            if dp[count][i] != -1:
                return dp[count][i]
            
            #Find the earliest event we can attend if we attend the current one i
            next_i = bisect_right(start_times, events[i][1])

            dp[count][i] = max(dfs(i+1, count), #Skip the current event
                               events[i][2] + dfs(next_i, count-1))
            
            return dp[count][i]
        
        return dfs(0, k)
        
# @lc code=end

