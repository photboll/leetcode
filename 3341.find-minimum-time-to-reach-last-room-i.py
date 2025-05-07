#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
from heapq import heappop, heappush
DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        dijsktras, start location 0, 0,0(time, i, j), target = (n-1, m-1)
        from a given position we can at the earliest get to a neighbor:
        1. Non need to visiti it if we already have processed it
        2. At the current time+1 if moveTIme of the neighbor is less
        3. at movetime + 1 if the
        """
        n = len(moveTime)
        m = len(moveTime[0])
        visited = set((0,0))# (i, j)
        heap = [(0,0,0)]

        while heap:
            curr_time, i, j = heappop(heap)
            if i == n-1 and j == m-1:
                return curr_time
            
            for di, dj in DIRECTIONS:
                ni, nj = i+di, j+dj
                if  0<= ni < n and 0<= nj < m and (ni, nj) not in visited:
                    visited.add((ni, nj)) 
                    heappush(heap, (max(curr_time, moveTime[ni][nj])+1, ni, nj))
        
        return -1
# @lc code=end

