#
# @lc app=leetcode id=3342 lang=python3
#
# [3342] Find Minimum Time to Reach Last Room II
#

# @lc code=start
from heapq import heappush, heappop
DIRECTIONS = [(0, 1), (0,-1), (1, 0), (-1, 0)]
    
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """Can we simply keep a state of if the previous move cost 1 or 3?
        We might end up in a situation were it would have been better to wait at position instead of moving from it
        but on the other hand the diference between an expensive move and a chep move is only 1
        
        """
        n = len(moveTime)
        m = len(moveTime[0])
        heap = [(0, 0, 0, 0)]  # (time, x, y, parity)
        dist = {(0,0,0): 0}

        while heap:
            curr_time, i, j, parity = heappop(heap)
            if i == n -1 and j == m-1:
                return curr_time
            #print(curr_time, move_duration, i, j)
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj
                if 0<= ni < n and 0<= nj < m :
                    arrival_time = max(curr_time, moveTime[ni][nj]) + 1+ parity
                    new_parity = not parity
                    if (ni, nj, new_parity) not in dist or arrival_time < dist[(ni, nj, new_parity)]:
                        dist[(ni, nj, new_parity)] = arrival_time
                        heappush(heap, (arrival_time, ni, nj, new_parity))
        return -1
                        

        
# @lc code=end

