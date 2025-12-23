#
# @lc app=leetcode id=2054 lang=python3
#
# [2054] Two Best Non-Overlapping Events
#

# @lc code=start
from collections import deque
from heapq import heappush, heappop
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])#sort on starttime

        #prefix max, what is the largest value we can have when we start s
        best_single = 0
        res = 0 
        heap = []
        for s, e, val in events:
            #which event have ended before the current one?
            #any event that have ended before the current start time
            #can be attended as well with the current one
            while heap and heap[0][0] < s:
                _, v = heappop(heap)
                best_single = max(best_single, v)
            
            res = max(res, best_single + val)
            heappush(heap, (e, val))

        return res
            
                

        
        
        
# @lc code=end

