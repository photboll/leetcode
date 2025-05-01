#
# @lc app=leetcode id=2071 lang=python3
#
# [2071] Maximum Number of Tasks You Can Assign
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        Any task that requires more than max(workers)+ strength is impossible ti complete,
        since we can only give one pill to a worker. 
        Each worker can only complete a single task. it is not stated in the problem but the examples seems to imply it
        The order in tasks and workers doe snot matter, so we can sort them as we please.
        Would trying to minimize the excessive strength (workers[j] - task[i]) for each pair lead to an optimal solution?
        not sure,
        
        We can start with trying to sort the tasks and workers in ascending order:
        then we can easily see if the easiest task can be completed (with or w/o a pill)
        by comapring task[0] and workers[0]
        what should we do when the weakest worker is too weak for the easiest task?
        is it better to skip this worker or use a pill?
        since we can only give one pill to a worker there is no need to delay using them.
        if we use a pill now, we can complete one more task 
        if we save the pill, we can atmost complete one more task later.
        The guarantted option is preferable. So we should never hesitate to use a pill if it would make a difference
        this is wrong.
        the current task may be solved easily be someone else, that would otherwise be left without task
        and the pill may be used for someone that can complete a task that no one else can complete without a pill
        """
        tasks.sort()
        workers.sort() 

        def can_assign_k(k) -> bool:
            p = pills
            ws = SortedList(workers[-k:])

            #Try to assign each task to a worker 
            for i in range(k-1, -1, -1):
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    #Find the worker that barely can complete it with a pill
                    candidate_w = ws.bisect_left(tasks[i] - strength)
                    if candidate_w == len(ws):
                        #Not even the strongest worker can complete it with a pill
                        return False
                    p -= 1#use the pill
                    ws.pop(candidate_w)
                    
            return True
            
        
        result = 0
        low, high = 0, min(len(tasks), len(workers))
        while low <= high:
            mid = (low + high) // 2
            if can_assign_k(mid):
                result = mid
                low = mid + 1
            else:
                high = mid -1
                
        return result 
        
# @lc code=end

