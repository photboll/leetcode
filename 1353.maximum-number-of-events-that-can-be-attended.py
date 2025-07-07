#
# @lc app=leetcode id=1353 lang=python3
#
# [1353] Maximum Number of Events That Can Be Attended
#

# @lc code=start
from heapq import heappush, heappop
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        heap = []
        res = 0
        j = 0
        for i in range(1, max_day+1):
            while j< n and events[j][0] <= i:
                heappush(heap, events[j][1])
                j+= 1
            while heap and heap[0] < i:
                heappop(heap)
            if heap:
                heappop(heap)
                res += 1
        return res

            

        
# @lc code=end

