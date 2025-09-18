#
# @lc app=leetcode id=3408 lang=python3
#
# [3408] Design Task Manager
#

# @lc code=start
from heapq import heapify, heappop, heappush
from collections import defaultdict

class TaskManager:
    """
    exectop cares about the global maximum task prio
    the heap needs to include all users 
    """

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.task2prio = {}
        self.task2user = {}

        for user_id, task_id, prio in tasks:
            #negative prio to turn min-heap into max-heap
            self.heap.append((-prio, -task_id))
            self.task2prio[task_id] = prio
            self.task2user[task_id] = user_id
        
        heapify(self.heap)
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.heap, (-priority, -taskId))
        self.task2prio[taskId] = priority
        self.task2user[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        if self.task2prio[taskId] != newPriority:
            heappush(self.heap, (-newPriority, -taskId))
            self.task2prio[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        del self.task2prio[taskId]
        del self.task2user[taskId]

    def execTop(self) -> int:
        #peek at the top element
        while self.heap:
            neg_prio, neg_id = heappop(self.heap)
            prio, task_id = -neg_prio, -neg_id
            #If the priority does not match, then the priority have changed
            if task_id in self.task2prio and self.task2prio[task_id] == prio:
                del self.task2prio[task_id]
                user_id = self.task2user[task_id]
                break
        else:
            return -1

        return user_id
    
        

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
# @lc code=end

