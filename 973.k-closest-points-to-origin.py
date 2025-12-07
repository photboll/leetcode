#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from math import sqrt
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(x1, y1, x2, y2):
            return sqrt((x2-x1)**2 + (y2-y1)**2)

        heap = []
        for (x, y) in points:
            d = dist(x, y, 0, 0)
            heappush(heap, (d, [x, y]))
        res = []
        for _ in range(k):
            d, point = heappop(heap)
            res.append(point)
        return res
        


            
        
        
# @lc code=end

