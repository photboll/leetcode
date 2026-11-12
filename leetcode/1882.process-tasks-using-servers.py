# @lc app=leetcode id=1882 slug=process-tasks-using-servers lang=python3
#
# [1882] Process Tasks Using Servers
# Difficulty: Medium
# Tags: Array, Heap (Priority Queue)
# URL: https://leetcode.com/problems/process-tasks-using-servers/
#
# @lc code=start

from collections import deque
from heapq import heappush, heappop, heapify


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        ans = [-1] * (len(tasks))
        available = [(w, srv_id) for srv_id, w in enumerate(servers)]
        heapify(available)
        #(time when available, srv_id)
        occupied = []
        
        cur_t = 0
        for j, t in enumerate(tasks):
            if j > cur_t:
                cur_t = j
            
            #if no server is free we will have to wait
            if not available:
                cur_t = max(cur_t, occupied[0][0])

            # Move servers which have finished their task at time j to the available pq 
            while occupied and occupied[0][0] <= cur_t :
                _ , srv_id = heappop(occupied)
                heappush(available, (servers[srv_id], srv_id))



            #lowest rank server should be assigned the task
            cur_srv = heappop(available)
            ans[j] = cur_srv[1]
            heappush(occupied, (cur_t + t, cur_srv[1]))


        return ans





            


        

# @lc code=end
