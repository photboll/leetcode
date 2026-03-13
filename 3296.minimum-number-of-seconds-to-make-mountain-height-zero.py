#
# @lc app=leetcode id=3296 lang=python3
#
# [3296] Minimum Number of Seconds to Make Mountain Height Zero
#

# @lc code=start
from heapq import *
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        """ 
        a min heap with the worker that is freshest. able to reduce the height the most 
        in a second
        
        pop the freshest worker.
            reduce the mountain
            add the time and push it back to the heap
        
        what should the heap have_
        (time to reduce 1, workers_index, time)
        No the heap is not storing the fastest worker. it is storing the earliest job completeion time 
        """

        #Stores (current_time, worker_time, units_done_so_far)
        pq = []
        for w_time in workerTimes:
            heappush(pq, (w_time, w_time, 1))
        

        while pq:
            #k is the number units of work this worker have completed
            cur_time, w_time, k = heappop(pq)
            mountainHeight -= 1
            if mountainHeight <= 0:
                return cur_time
            heappush(pq, (cur_time + (k+1)*w_time, w_time, k+1))
        


        
class SolutionBS:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        
        
        low = 0
        high = pow(10, 9) + 7

        while low < high:
            mid = (high + low + 1) // 2
            if possible(mid):
                low = mid
            else:
                high = mid - 1

        return low 
        
# @lc code=end

