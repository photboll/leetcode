# @lc app=leetcode id=1606 slug=find-servers-that-handled-most-number-of-requests lang=python3
#
# [1606] Find Servers That Handled Most Number of Requests
# Difficulty: Hard
# Tags: Array, Heap (Priority Queue), Simulation, Ordered Set
# URL: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
#
# @lc code=start
from heapq import heapify, heappop, heappush
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        count = [0] * k
        busy = [] # (end_time, srv_id)
        free = list(range(k))

        for i, (a, l) in enumerate(zip(arrival, load)):
            # release finished servers
            while busy and busy[0][0] <= a:
                _, s = heappop(busy) 
                #push with the smallest index i + ((s-i) %k) that is >= i
                heappush(free, i + ((s-i) %k))
            
            while free and free[0] < i:
                s = heappop(free) % k
                heappush(free, i + ((s-i)%k))
            

            #drop if no available server
            if not free:#drop 
                continue
            
            s = heappop(free) % k
            count[s] += 1
            heappush(busy, (a+l, s))
        
        m = max(count)
        return [i for i, c in enumerate(count) if c == m]



        

# @lc code=end
